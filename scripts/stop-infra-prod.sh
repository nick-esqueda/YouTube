# RUN THIS SCRIPT FROM THE PROJECT ROOT DIRECTORY.

if [ -f scripts/.env ]; then
  source scripts/.env
else 
  echo "ERROR: .env file must exist in the ./scripts/ directory. Aborting script."
  exit 1
fi

cd backend/
pwd

echo 'triggering RDS DB shutdown...'

aws rds stop-db-instance \
--no-cli-pager \
--db-instance-identifier $RDS_DB_INSTANCE_ID_PROD \
--profile $AWS_PROFILE 

echo 'removing load balancer from EB environment...'

cd .elasticbeanstalk
eb config youtube-prod \
--update file://update-to-single-instance-env.yml \
--profile $AWS_PROFILE 
cd ..

echo 'scaling EC2 instances down to 0...'

aws autoscaling update-auto-scaling-group \
--auto-scaling-group-name $AUTO_SCALING_GROUP_NAME_PROD \
--min-size 0 \
--max-size 1 \
--desired-capacity 0 \
--profile $AWS_PROFILE 

echo 'script completed. some AWS processes may still be running.'
