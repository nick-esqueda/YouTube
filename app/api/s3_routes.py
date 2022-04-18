import os
import boto3
import requests
import random
import string
from flask import Blueprint, jsonify, request
# from botocore.config import Config


s3_routes = Blueprint('s3_routes', __name__)


@s3_routes.route('/upload/video', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return jsonify('error')

    file = request.files['file']

    OBJECT_NAME= ''.join(random.choices(string.ascii_lowercase + string.digits, k=30))

    s3_client = boto3.client('s3')

    response = s3_client.generate_presigned_post(
        Bucket=os.environ.get('AWS_BUCKET_NAME'),
        Key=OBJECT_NAME,
        Fields={ "Content-Type": "video/mp4" },
        Conditions=[{ "Content-Type": "video/mp4" }],
        ExpiresIn=60
    )

    uploadFile = {'file': (OBJECT_NAME, file)}
    
    requests.post(response['url'], data=response['fields'], files=uploadFile)
    
    url  = response['url'] + response['fields']['key']
    return jsonify(url)
