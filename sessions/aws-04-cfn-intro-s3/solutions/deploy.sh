#!/bin/sh

###
### Script to deploy S3 bucket in cloudformation stack
###

#### CONFIGURATION SECTION ####
aws_profile="$1" # e.g. sot-academy, for the aws credentials
your_name="$2" # e.g. rory-gilmore, for the stack name
#### CONFIGURATION SECTION ####

# Deploy the stack
echo ""
echo "Doing etl stack deployment..."
echo ""
aws cloudformation deploy --stack-name ${your_name}-shopper-etl-pipeline \
    --template-file etl-stack.yml --region eu-west-1 \
    --capabilities CAPABILITY_IAM \
    --profile ${aws_profile} \
    --parameter-overrides \
      YourName="${your_name}";

echo ""
echo "...all done!"
echo ""
