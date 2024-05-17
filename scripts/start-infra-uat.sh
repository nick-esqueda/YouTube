# RUN THIS SCRIPT FROM THE PROJECT ROOT DIRECTORY.

if [ -f scripts/.env ]; then
  source scripts/.env
else 
  echo "ERROR: .env file must exist in the ./scripts/ directory. Aborting script."
  exit 1
fi

cd backend/
pwd

echo 'triggering RDS DB startup...'

aws rds start-db-instance \
--no-cli-pager \
--db-instance-identifier $RDS_DB_INSTANCE_ID_UAT \
--profile $AWS_PROFILE 

echo 'enabling load balancer in EB environment...'

cd .elasticbeanstalk
eb config youtube-uat \
--update file://update-to-load-balanced-env.yml \
--profile $AWS_PROFILE 
cd ..

echo 'scaling EC2 instances up to 1...'

aws autoscaling update-auto-scaling-group \
--auto-scaling-group-name $AUTO_SCALING_GROUP_NAME_UAT \
--min-size 1 \
--max-size 1 \
--desired-capacity 1 \
--profile $AWS_PROFILE 

echo 'script completed. some AWS processes may still be running.'
