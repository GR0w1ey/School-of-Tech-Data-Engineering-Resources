# aws-06-cfn-lambda-exercise.md

## Stack template

We need to start from the partially complete file [../handouts/etl-stack.yml](../handouts/etl-stack.yml)

> Values and further steps can be found in the slides for this section

- Add a parameter for Network Stack Name, so we know where to put the lambda
- Add a Lambda with a dynamic name (from Your Name)
- Add a Notification Configuration to the CSV bucket, so that files arriving there wake up the lambda
- Add dependencies to the CSV Bucket
- Add a Source Bucket Permission, so the Lambda is allowed to look in the bucket

## Deployment

First:

- Log in depending on your AWS login method
    - If on windows, you may need to run the below commands in PowerShell
- Run
    - Either `aws sso login --profile <your-profile-name>`
    - or `aws-azure-login --profile <you-profile-name>`

Then:

- Open a terminal in the [handouts](../handouts/) folder
    - If using Windows this may need to be in GitBash
- Deploy your stack using [../handouts/deploy.sh](../handouts/deploy.sh)
    - Your user-name must be entered like `lowercase-with-dashes` as it will be used in the S3 Bucket names as well.
    - e.g `./deploy.sh <your-profile-name> <your-name>`
    - i.e `./deploy.sh sot-academy rory-gilmore`

## Validation

- Open the AWS (web) console and check the deployment
    - Check the CloudFormation events on your Stack
    - Check the bucket
    - Check your Log Group for the latest Log Stream
