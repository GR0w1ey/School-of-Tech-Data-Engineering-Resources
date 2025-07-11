# Making aws-azure-logon work in Windows for SoT

Due to Accenture security posture changes, WSL is now completely blocked from being able to log into Accenture systems (it does not count as part of the validated operating system on your machine).

For Windows users, we now use the following instructions in this file (tl;dr - use PowerShell).

> For School of Tech users on MacOS and Unix, please use file [./aws-setup-azure-login.md](./aws-setup-azure-login.md).
>
> For Windows users, please continue to use this file

## Native Windows solution

### Pre-requisites

- In windows, install the AWS CLI tools
    - Download the [latest AWS CLI version](https://awscli.amazonaws.com/AWSCLIV2.msi)
    - Open the download and follow the installation steps
    - Verify your installation by running `aws --version` in a Powershell terminal
- In Admin Powershell, install `chocolatey` if you do not already have it
    - See <https://chocolatey.org/install#individual>
- In Admin Powershell, use chocolatey to install `node` by running:
    - `choco install -y nodejs-lts`
    - Close the powershell window
    - Open a new Admin Powershell window
    - Check the installation by running `node --version` and `npm --version`
- In Admin Powershell, use node to install `aws-azure-login` by running:
    - `npm install -g aws-azure-login`
- In Powershell, run `echo $PROFILE` to find where your ps config file should be
    - This should print something like `C:\users\rory.gilmore\Documents\PowerShell\Profile.ps1\Microsoft.PowerShell_profile.ps1`
- Open it by running `code "$PROFILE"` in a PowerShell window
    - It should open a moment later in VSCode
    - Check the path that opens in VSCode is correct (in case of spaces etc)
    - In the file set two environment variables, like so:
        - `$Env:PUPPETEER_EXECUTABLE_PATH='C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'`
    - and
        - `$Env:AWS_PROFILE='sot-academy'`
    - Save and close the file
- Close all open Powershell terminals

### Configuring the aws-azure-login tool

In Powershell, we will configure aws-azure-login, but first we need some data:

- The instructor will now give you three sensitive bits of data. Do not put these into Git, or share them anywhere:
    - `azure_tenant_id` e.g. `abc-de-fgh-ij`
    - `azure_app_id_uri` e.g. `klm-nop-qrst`
    - `aws_account_number` e.g. `9876543210`
- You will also need:
    - `full_accenture_email_address` E.g. `rory.gilmore@accenture.com`
    - `iam_role_arn`, which is long and looks something like this: `arn:aws:iam::{aws_account_number}:role/student-access-role`,
        e.g. `arn:aws:iam::9876543210:role/student-access-role`
    - `aws_region`, e.g. `eu-west-1`

Now we can configure the tool:

- Open a new Admin Powershell window
- Run this:
    - `aws-azure-login --configure --profile sot-academy`
- Substitute in the values from above when prompted (The core SoT team has the details):

    ```sh
    Azure Tenant ID: {azure_tenant_id}
    Azure App ID URI: {azure_app_id_uri}
    Default Username: {full_accenture_email_address}
    Stay logged in: true
    Default Role ARN: {iam_role_arn}
    Default Session Duration Hours: 1
    Region: {aws_region}
    ```

- Also set your default region by running:
    - `aws configure set region eu-west-1 --profile sot-academy`
- In Edge on windows, log into any Accenture sites (like [Workday](workday.accenture.com)) so that you have the relevant cookies set in advance
- In your Admin Powershell, use this to log in:
    - `aws-azure-login --mode gui --profile sot-academy`
    - on some machines `--mode cli` will also work, if `gui` does not
- Then running `aws s3 ls --profile sot-academy` should show you the list of Buckets
- All done!
