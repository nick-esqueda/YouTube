cd backend/
pwd

echo "This script will start the PROD EB environment (DB, EC2 instances, ELB). Are you sure you want to proceed? (yes/no)"
read confirmation

if [ "$confirmation" == "yes" ]; then
    echo "Proceeding with the rest of the script..."
else
    echo "Script aborted."
    exit 1
fi

echo 'triggering RDS DB startup...'
aws rds start-db-instance --no-cli-pager --db-instance-identifier awseb-e-8cucwt8iij-stack-awsebrdsdatabase-jfnalsxu5jlf

echo 'enabling load balancer...'
cd .elasticbeanstalk
eb config youtube-prod --update file://update-to-load-balanced-env.yml
cd ..

echo 'scaling up EC2 instances to 1...'
aws autoscaling update-auto-scaling-group \
--auto-scaling-group-name awseb-e-8cucwt8iij-stack-AWSEBAutoScalingGroup-mctoWswbQr2G \
--min-size 1 \
--max-size 1 \
--desired-capacity 1

echo 'script completed. some AWS processes may still be running.'
