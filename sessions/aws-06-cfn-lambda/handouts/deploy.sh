#!/bin/sh

###
### Script to deploy S3 bucket + lambda in cloudformation stack
###

#### CONFIGURATION SECTION ####
aws_profile="$1" # e.g. sot-academy, for the aws credentials
your_name="$2" # e.g. rory-gilmore, for the stack name
deployment_bucket="${your_name}-shopper-deployment-bucket"
#### CONFIGURATION SECTION ####

# Create deployment bucket stack
echo ""
echo "Doing deployment bucket stack..."
echo ""
aws cloudformation deploy --stack-name "${deployment_bucket}" \
    --template-file deployment-bucket-stack.yml --region eu-west-1 \
    --capabilities CAPABILITY_IAM --profile ${aws_profile} \
    --parameter-overrides \
      YourName="${your_name}";

# If SKIP_PIP_INSTALL variable is not set or is empty then do a pip install
if [ -z "${SKIP_PIP_INSTALL:-}" ]; then
    echo ""
    echo "Doing pip install..."
    # Install dependencies from requirements-lambda.txt into src directory with python 3.12
    # On windows may need to use `py` not `python3`
    python3 -m pip install --platform manylinux2014_x86_64 \
        --target=./src --implementation cp --python-version 3.12 \
        --only-binary=:all: --upgrade -r requirements-lambda.txt;
else
    echo ""
    echo "Skipping pip install"
fi

# Package template and upload local resources to S3
# A unique S3 filename is automatically generated each time
echo ""
echo "Doing packaging..."
echo ""
aws cloudformation package --template-file etl-stack.yml \
    --s3-bucket ${deployment_bucket} \
    --output-template-file etl-stack-packaged.yml \
    --profile ${aws_profile};

# Deploy template pointing to packaged resources
echo ""
echo "Doing etl stack deployment..."
echo ""
aws cloudformation deploy --stack-name "${your_name}-shopper-etl-pipeline" \
    --template-file etl-stack-packaged.yml --region eu-west-1 \
    --capabilities CAPABILITY_IAM \
    --profile ${aws_profile} \
    --parameter-overrides \
      YourName="${your_name}";

echo ""
echo "...all done!"
echo ""
