---
title: AWS 02 - CLI Setup
---

## AWS 02 - CLI Setup

---

### AWS sessions list

- AWS 01 AWS + Cloud Intro ✅ _1.5hrs_
- AWS 02 AWS CLI Setup ⬅ _1.5hrs_
- AWS 03 S3 Storage (Console) _1.5hrs_
- AWS 04 CloudFormation Intro + S3 Storage (IaC) _1.5hrs_
- AWS 05 Lambda Intro _1.5hrs_
- AWS 06 Lambda (IaC) _1.5hrs_
- AWS 07 Redshift (IaC) _1.5hrs_
- AWS 08 EC2 (IaC) + Grafana setup _1.5hrs_

---

### Overview

- What is the AWS CLI?
- Installing the AWS CLI
- Installing SSO tools to help us authenticate

---

### Learning Objectives

- Explain why the AWS CLI is useful to us as engineers
- Understand how to install the AWS CLI on our laptops
- Understand how to configure authentication via SSO with the AWS CLI

---

### AWS CLI

![](img/cli.svg) <!-- .element: class="centered" height="350px" -->

---

### AWS CLI

- The way we interact with AWS services through the CLI (Command Line Interface)
- Ease of use over logging in to the console
- If you can do it on the Console, you can do it in the CLI - YAY!
- Simple use-cases: searching logs, quick S3 upload/download

---

### CLI Installation

Let's install the CLI, so that once we're done we'll be able to communicate with AWS via the command line:

```sh
$ aws <command> <subcommand> [options and parameters]
```

Notes: You may have done this already in Laptop Setup sessions

---

### Installing the CLI - Windows

- Download the [latest version](https://awscli.amazonaws.com/AWSCLIV2.msi)
- Open the download and follow the installation steps
- Verify your installation with the following command:

```sh
C:\> aws --version
aws-cli/2.1.24 Python/3.7.4 Windows/10 botocore/2.0.0
```

Note - You may see a more recent version number.

---

### Installing the CLI - MacOS

- Download the [latest version](https://awscli.amazonaws.com/AWSCLIV2.pkg)
- Open the download and follow the installation steps
- Verify your installation with the following commands:

```sh
$ which aws
/usr/local/bin/aws

$ aws --version
aws-cli/2.1.24 Python/3.7.4 Darwin/18.7.0 botocore/2.0.0
```

Note - you may see a more recent version number.

---

### Installing the CLI - Linux

Follow the guide which best matches your setup [here](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html).

---

### Emoji Check:

How do you feel about the CLI installation process?

Do you feel you understand why the AWS CLI is useful?

1. 😢 Haven't a clue, please help!
2. 🙁 I'm starting to get it but need to go over some of it please
3. 😐 Ok. With a bit of help and practice, yes
4. 🙂 Yes, with team collaboration could try it
5. 😀 Yes, enough to start working on it collaboratively

Notes:
The phrasing is such that all answers invite collaborative effort, none require solo knowledge.

The 1-5 are looking at (a) understanding of content and (b) readiness to practice the thing being covered, so:

1. 😢 Haven't a clue what's being discussed, so I certainly can't start practising it (play MC Hammer song)
2. 🙁 I'm starting to get it but need more clarity before I'm ready to begin practising it with others
3. 😐 I understand enough to begin practising it with others in a really basic way
4. 🙂 I understand a majority of what's being discussed, and I feel ready to practice this with others and begin to deepen the practice
5. 😀 I understand all (or at the majority) of what's being discussed, and I feel ready to practice this in depth with others and explore more advanced areas of the content

---

<!-- .slide: data-only="generation jlr sainsburys" -->
### Configuring aws sso

We will use a command called `aws sso` to handle logging into AWS via the CLI.

- On a terminal, run `aws configure sso`
- When it asks for `SSO session name`, enter a reasonable name, such as `de-course`
- Enter your SSO (_Single Sign-On_) URL (if you don't know it, your instructor will be able to tell you - it will likely be something like `https://<bootcamp-name>.awsapps.com/start#/`)
- Enter the SSO Region, which should be `eu-west-1`
- When it asks for _SSO registration scopes_, hit enter

---

<!-- .slide: data-only="generation jlr sainsburys" -->
### Configuring aws sso

- A webpage will open asking you to sign into the AWS CLI, click the `*Sign in to AWS CLI*` button
- Looking back at your terminal, you will see some text which looks something like this:
   > Using the account ID _xxxxxxxxxxxx_<br />
   > The only role available to you is: StudentAccess <br />
   > Using the role name "StudentAccess"

---

<!-- .slide: data-only="generation jlr sainsburys" -->
### Configuring aws sso

- When it asks for _CLI default client Region_, enter `eu-west-1`
- When it asks for _CLI default output format_, enter `json`
- When it asks for _CLI profile name_, enter the same name as above e.g. `de-course`
- Check your login works
    - Run `aws sso login --profile <profile-name>` in your terminal (i.e. use the _CLI profile name_ you entered above)

---

<!-- .slide: data-only="generation jlr sainsburys" -->
### Configuring aws sso

#### That's all (for now!)

You can log out of your SSO any time by running `aws sso logout` in your terminal.

You can now login any time by running `aws sso login --profile <profile-name>` in your terminal.

---

<!-- .slide: data-only="schooloftech" -->
### SoT - Windows setup

> See handout [./handouts/README-windows-setup-SoT.md](./handouts/README-windows-setup-SoT.md) for all users on Windows
>
> Windows users only!

If you are using GitBash on Windows - we will not be using that at all for AWS logins, sorry.

---

<!-- .slide: data-only="schooloftech" -->
### SoT - MacOs / Unix setup

> See handout [./handouts/aws-setup-azure-login.md](./handouts/aws-setup-azure-login.md).
>
> MacOs / Unix users only!

---

<!-- .slide: data-only="schooloftech" -->
### Logging into AWS

Run the following command to log in to AWS:

```sh
aws-azure-login --profile <profile-name> --mode gui
# or
aws-azure-login --profile <profile-name> --mode cli
```

You will be prompted to enter your Accenture account password, you can copy/paste this into your terminal.

---

<!-- .slide: data-only="schooloftech" -->
### Adding aliases (MacOS / Unix)

We can add some handy aliases or "fake commands" to our `~/.bashrc` or `~/.zshrc` file for use later:

```sh
alias aws-logon='aws-azure-login --profile <profile-name>'
alias aws-logon-cli='aws-azure-login --profile <profile-name> --mode cli'
alias aws-logon-gui='aws-azure-login --profile <profile-name> --mode gui'
alias awsconf='nano ~/.aws/config'
alias awscreds='nano ~/.aws/credentials'
alias codeawsconf='code ~/.aws/config'
alias codeawscreds='code ~/.aws/credentials'
```

Add the examples above and re-source your file (or open a new terminal).

Notes:
Would need a volunteer to double check this but on Windows to set aliases in PowerShell:

- Run `code $PROFILE` or `notepad $PROFILE`
- Add the following line to set an alias `Set-Alias <alias-name> <command>`. Can use `Get-ChildItem` as an example which is the Windows equivalent of `ls`
- Save and source the file by doing `. $PROFILE`

---

### Confirming your CLI access

- On your terminal, check which user you're using to call the AWS operations:
    - `aws sts get-caller-identity --profile <profile-name>`
- Get a list of available S3 buckets:
    - `aws s3 ls --profile <profile-name>`

---

### Confirming your Console access

- On the Management Console in your browser:
    - Search for S3 in the services search box at the top of the page
    - Select S3 from the list of services
    - Look at the list of available buckets - does this match what you saw in the terminal?

We'll hear more info on what "S3" and "buckets" are in the next session!

---

<!-- .slide: data-only="schooloftech" -->
### Emoji Check:

How do you feel about the `aws-azure-login` installation process?

Do you feel you understand why the AWS CLI is useful?

1. 😢 Haven't a clue, please help!
2. 🙁 I'm starting to get it but need to go over some of it please
3. 😐 Ok. With a bit of help and practice, yes
4. 🙂 Yes, with team collaboration could try it
5. 😀 Yes, enough to start working on it collaboratively

Notes:
The phrasing is such that all answers invite collaborative effort, none require solo knowledge.

The 1-5 are looking at (a) understanding of content and (b) readiness to practice the thing being covered, so:

1. 😢 Haven't a clue what's being discussed, so I certainly can't start practising it (play MC Hammer song)
2. 🙁 I'm starting to get it but need more clarity before I'm ready to begin practising it with others
3. 😐 I understand enough to begin practising it with others in a really basic way
4. 🙂 I understand a majority of what's being discussed, and I feel ready to practice this with others and begin to deepen the practice
5. 😀 I understand all (or at the majority) of what's being discussed, and I feel ready to practice this in depth with others and explore more advanced areas of the content

---

<!-- .slide: data-visibility="hidden" -->
### Terms and Definitions - recap

TODO

---

### Overview - recap

- What is the AWS CLI?
- Installing the AWS CLI
- Authenticating with the AWS CLI

---

### Learning Objectives - recap

- Explain why the AWS CLI is useful to us as engineers
- Understand how to install the AWS CLI on our laptops
- Understand how to configure authenticating via SSO with the AWS CLI

---

<!-- .slide: data-only="generation jlr sainsburys" -->
### Further Reading

- [AWS CLI Documentation](https://docs.aws.amazon.com/cli/)

---

<!-- .slide: data-only="schooloftech" -->
### Further Reading

- [AWS CLI Documentation](https://docs.aws.amazon.com/cli/)
- [aws-azure-login homepage](https://github.com/aws-azure-login/aws-azure-login)

---

### Emoji Check:

On a high level, do you think you understand the main concepts of this session? Say so if not!

1. 😢 Haven't a clue, please help!
2. 🙁 I'm starting to get it but need to go over some of it please
3. 😐 Ok. With a bit of help and practice, yes
4. 🙂 Yes, with team collaboration could try it
5. 😀 Yes, enough to start working on it collaboratively

Notes:
The phrasing is such that all answers invite collaborative effort, none require solo knowledge.

The 1-5 are looking at (a) understanding of content and (b) readiness to practice the thing being covered, so:

1. 😢 Haven't a clue what's being discussed, so I certainly can't start practising it (play MC Hammer song)
2. 🙁 I'm starting to get it but need more clarity before I'm ready to begin practising it with others
3. 😐 I understand enough to begin practising it with others in a really basic way
4. 🙂 I understand a majority of what's being discussed, and I feel ready to practice this with others and begin to deepen the practice
5. 😀 I understand all (or at the majority) of what's being discussed, and I feel ready to practice this in depth with others and explore more advanced areas of the content
