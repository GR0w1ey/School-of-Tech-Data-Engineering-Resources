# aws-04-cfn-intro-exercise

## Stack template

We need to start from the mostly empty file [../handouts/etl-stack.yml](../handouts/etl-stack.yml).

- There is already a parameter for your name
- Add a valid S3 bucket using your name
    - Find the `# TODO add ShopperRawDataBucket` comment in the file
    - Add it, following the slides
- Add the bucket policy we need
    - Find the `# TODO Add ShopperRawDataBucketPolicy` comment in the file
    - Add it, following the slides

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

- Open the AWS (web) Console for CloudFormation and check the deployment
    - Check the CloudFormation events on your Stack
    - Check the bucket
