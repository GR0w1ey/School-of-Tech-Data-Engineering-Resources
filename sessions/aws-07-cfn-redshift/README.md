# AWS 07 - Intro to Amazon Redshift + Redshift with IaC

Here we introduce Redshift as a Big Data database, and connect to it using Python and data from the Parameter Store.

A fully worked example is in the [data-academy-pipeline-example repo](https://github.com/infinityworks/data-academy-pipeline-example).

> To save costs this session is run with one database per project team in a single shared redshift cluster.
>
> Before the session the instructors must set up the shared redshift cluster and a database per team (see "Prep" session below).

## Related documents

> Important! You will find these useful for reference:

- Main [../README.md](../README.md), `Final Project (second half of course)` section
- Main [../README.md](../README.md), `Related Documents` section for
    - Related repos
    - Team project documents!

## Overview

- Before Data Warehouses
- Redshift as a Data Warehouse
- Connecting from a lambda using Python

## AWS sessions list

This is the list of AWS sessions done so far, and the following ones:

- AWS 01 AWS + Cloud Intro ✅ _1.5hrs_
- AWS 02 AWS CLI Setup ✅ _1.5hrs_
- AWS 03 S3 Storage (Console) ✅ _1.5hrs_
- AWS 04 CloudFormation Intro + S3 Storage (IaC) ✅ _1.5hrs_
- AWS 05 Lambda Intro ✅ _1.5hrs_
- AWS 06 Lambda (IaC) ✅ _1.5hrs_
- AWS 07 Redshift (IaC) ⬅ _1.5hrs_
- AWS 08 EC2 (IaC) + Grafana setup _1.5hrs_
- AWS 09 Queues _1.5hrs_
- AWS 10 Monitoring _1.5hrs_

## Timings

- This session is timetabled for 1 block at 1.5 hrs, i.e. 0.25 elapsed training days

## Assessments

To check the learner progress in this session we have:

- Follow-along exercises to use the AWS CLI with CloudFormation templates
- Emoji Checks to confirm learner understanding and progress
- Breakouts for connecting to the team databases

## Prep - Redshift Cluster and databases

> Before the session the instructors must set up the shared redshift cluster and a database per team
>
> This means the final project teams must already be organised, and breakouts for this session should be per-team.

We set up one database in the cluster for each project team on the course:

- This is covered in detail at [data-academy-final-project-infrastructure/#add-redshift-cluster](https://github.com/infinityworks/data-academy-final-project-infrastructure?tab=readme-ov-file#add-redshift-cluster)

## Prep - standard

- Create the session files (pdf and zip) for distribution using `make generate-session-files f=module_name` or `make gsf-local f=module_name`
- Ensure you can authenticate to AWS using the correct credentials for the course (e.g. School of Tech, Generation, Client, etc.)

## Session

- See all the critical prep above
- Run the slides
- Demo the IaC yourself, show it working
- Demo the lambda code, show it working
- Demo the lambda triggering from CSV, show it working
- Then have breakouts per project team
