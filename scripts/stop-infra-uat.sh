cd app/
pwd

echo 'triggering RDS DB shutdown...'
aws rds stop-db-instance --no-cli-pager --db-instance-identifier awseb-e-ksevu6pfav-stack-awsebrdsdatabase-4gec0bh31ozn

echo 'killing load balancer...'
cd .elasticbeanstalk
eb config youtube-uat --update file://update-to-single-instance-env.yml
cd ..

echo 'scaling down EC2 instances to 0...'
aws autoscaling update-auto-scaling-group \
--auto-scaling-group-name awseb-e-ksevu6pfav-stack-AWSEBAutoScalingGroup-DiwoQoSrkJO5 \
--min-size 0 \
--max-size 1 \
--desired-capacity 0

echo 'script completed successfully. some AWS processes may still be running.'
