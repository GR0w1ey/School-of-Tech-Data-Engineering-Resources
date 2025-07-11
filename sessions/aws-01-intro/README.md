# AWS 01 - Intro to Cloud + AWS

An overview and introduction to cloud computing in AWS.

Following sessions are listed in the "AWS sessions list" section below.

## Related documents

> Important! You will find these useful for reference:

- Main [../README.md](../README.md), `Final Project (second half of course)` section
- Main [../README.md](../README.md), `Related Documents` section for
    - Related repos
    - Team project documents!

## Overview

- What is AWS?
- AWS Console
- IAM (Identity and Access Management)

## AWS sessions list

This is the list of AWS sessions done so far, and the following ones:

- AWS 01 AWS + Cloud Intro ⬅ _1.5hrs_
- AWS 02 AWS CLI Setup _1.5hrs_
- AWS 03 S3 Storage (Console) _1.5hrs_
- AWS 04 CloudFormation Intro + S3 Storage (IaC) _1.5hrs_
- AWS 05 Lambda Intro _1.5hrs_
- AWS 06 Lambda (IaC) _1.5hrs_
- AWS 07 Redshift (IaC) _1.5hrs_
- AWS 08 EC2 (IaC) + Grafana setup _1.5hrs_

## Timings

- This session is timetabled for 1 block at 1.5 hrs, i.e. 0.25 elapsed training days

## Assessments

To check the learner progress in this session we have:

- Follow-along exercises to use the AWS Console (Web)
- Emoji Checks to confirm learner understanding and progress

## Prep

- Ensure you can authenticate to AWS using the correct credentials for the course (e.g. School of Tech, Generation, Client, etc.)
- Make sure the slides for accessing AWS are up to date and match closely what you have to do - for example if Generation or a Client have updated anything recently, raise a PR to bring the slides in line
- Create the session files (pdf and zip) for distribution using `make generate-session-files f=module_name` or `make gsf-local f=module_name`

### Prep - required roles (School of Tech)

Make sure you have run the commands for the AWS and Team Project setup in advance:

- The instructions are here: [repo data-academy-final-project-infrastructure#commands-to-deploy](https://github.com/infinityworks/data-academy-final-project-infrastructure#commands-to-deploy)
- This creates the roles that you and the learners will need in this session and/or the next few weeks:
    - `lambda-execution-role`
    - `de-academy-ec2-role` and `de-academy-ec2-role-instance-profile`
    - `github-cicd-role`
    - `ScopePermissions` policy for use as a Permissions Boundary

### Prep - AWS console and CLI setup

Depending on the programme being delivered, share the appropriate `aws-setup-*.md` file with the cohort:

| Academy        | Setup File                                                                 |
|----------------|----------------------------------------------------------------------------|
| Generation     | [./handouts/aws-setup-sso.md](./handouts/aws-setup-sso.md)                 |
| School of Tech | [./handouts/aws-setup-azure-login.md](./handouts/aws-setup-azure-login.md) |

These instructions are covered in the slides but are a useful addition.

## Session

1. Have AWS console and/or CLI ready to use
1. Run the slide deck
1. When setting up access, give out the relevant handouts, as above
