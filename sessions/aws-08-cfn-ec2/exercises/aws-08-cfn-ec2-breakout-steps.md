# AWS 08 - EC2 and Grafana with CloudFormation

> This exercise is done as a code-along with the whole class during the session.
>
> The summary steps are re-created here.

## Stack template

We need to start from the partially complete file [../handouts/etl-stack.yml](../handouts/etl-stack.yml)

For further details refer to the slides and solutions folder (deliberately not duplicated here):

- Add CF Parameters for
    - `EC2InstanceProfileRoleName`
    - `EC2InstanceIngressIp`
    - `EC2UserData`
- Add a `GrafanaEc2Instance` resource with the right type and properties

## Deployment

First:

- Log in depending on your AWS login method
    - If on windows, you may need to run the below commands in PowerShell
- Run
    - Either `aws sso login --profile <your-profile-name>`
    - or `aws-azure-login --profile <you-profile-name>`

Then:

- Find your laptops public IP address from e.g. <https://whatsmyip.org>
- Open a terminal in the [handouts](../handouts/) folder
    - If using Windows this may need to be in GitBash
- Deploy your stack using [../handouts/deploy.sh](../handouts/deploy.sh)
    - Your user-name must be entered like `lowercase-with-dashes` as it will be used in the S3 Bucket names as well
    - Your team-name must be entered like `lowercase-with-dashes` as it will be used to lookup your redshift connection details in Parameter Store
    - Like `./deploy.sh <aws_profile> <your-name> <team-name> <your-ip>`
    - E.g. `./deploy.sh sot-academy rory-gilmore la-vida-mocha 12.34.56.78`

## Deployment Validation

- Open the AWS (web) console and check the deployment
    - Check the CloudFormation events on your Stack

## Grafana

Follow the steps in the slides to

- Log into Grafana
- Connect Grafana to Redshift
- Add settings for a data source
- Test the data source
- Add a visualisation

All done!
