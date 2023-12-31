cd app/
pwd

echo "This script will shut down the PROD EB environment (DB, EC2 instances, ELB). Are you sure you want to proceed? (yes/no)"
read confirmation

if [ "$confirmation" == "yes" ]; then
    echo "Proceeding with the rest of the script..."
else
    echo "Script aborted."
    exit 1
fi

echo 'triggering RDS DB shutdown...'
aws rds stop-db-instance --no-cli-pager --db-instance-identifier awseb-e-8cucwt8iij-stack-awsebrdsdatabase-jfnalsxu5jlf

echo 'killing load balancer...'
cd .elasticbeanstalk
eb config youtube-prod --update file://update-to-single-instance-env.yml
cd ..

echo 'scaling down EC2 instances to 0...'
aws autoscaling update-auto-scaling-group \
--auto-scaling-group-name awseb-e-8cucwt8iij-stack-AWSEBAutoScalingGroup-mctoWswbQr2G \
--min-size 0 \
--max-size 1 \
--desired-capacity 0

echo 'script completed successfully. some AWS processes may still be running.'
