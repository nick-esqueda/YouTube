cd app/
pwd

echo 'triggering RDS DB startup...'
aws rds start-db-instance --no-cli-pager --db-instance-identifier awseb-e-ksevu6pfav-stack-awsebrdsdatabase-4gec0bh31ozn

echo 'enabling load balancer...'
cd .elasticbeanstalk
eb config youtube-uat --update file://update-to-load-balanced-env.yml
cd ..

echo 'scaling up EC2 instances to 1...'
aws autoscaling update-auto-scaling-group \
--auto-scaling-group-name awseb-e-ksevu6pfav-stack-AWSEBAutoScalingGroup-DiwoQoSrkJO5 \
--min-size 1 \
--max-size 1 \
--desired-capacity 1

echo 'script completed successfully. some AWS processes may still be running.'
