# Queues

In this module we will be introducing the learners to queues and topics using Amazon SQS and SNS.

We will discuss what a queue is and why you might want to use one, as well as some of the associated considerations that should be taken and design patterns that can be implemented.

We will live demo the creation of a queue, dead-letter queue, SNS topic and subscription. Learners will be asked to integrate queues into the existing codebase for their projects.

Related sessions cover:

- [AWS intro + services](../aws/README.md)
- [DevOps inc. CI](../devops/README.md)
- [Cloudformation inc. CD](../cloudformation/README.md)
- [Data Warehousing inc. mention of Redshift](../data-warehousing/README.md)
- [Monitoring](../monitoring/README.md)
- [Queues inc SQS](../queues/README.md)
- [Data Streams inc Kinesis](../data-streams/README.md)

## Overview

- Message Queues
- Event Driven Design
- Pub/Sub Model and Notifications

## AWS sessions list

This is the list of AWS sessions done so far, and the following ones:

- AWS 01 AWS + Cloud Intro ✅ _1.5hrs_
- AWS 02 AWS CLI Setup ✅ _1.5hrs_
- AWS 03 S3 Storage (Console) ✅ _1.5hrs_
- AWS 04 CloudFormation Intro + S3 Storage (IaC) ✅ _1.5hrs_
- AWS 05 Lambda Intro ✅ _1.5hrs_
- AWS 06 Lambda (IaC) ✅ _1.5hrs_
- AWS 07 Redshift (IaC) ✅ _1.5hrs_
- AWS 08 EC2 (IaC) + Grafana setup ✅ _1.5hrs_
- AWS 09 Queues ⬅ _1.5hrs_
- AWS 10 Monitoring _1.5hrs_

## Timings

- This session is timetabled for 2 blocks at 1.5 hrs each, i.e. 0.5 elapsed training days
- The formative assessments occur during this and are included in that timing

## Assessments

To check the learner progress in this session we have:

- Multiple Quizzes throughout the session with answer walkthrough
- Follow along demo for the students

## Prep

- Create the session files (pdf and zip) using `make generate-session-files f=module_name`
- Review the slides and exercises
- The instructor will need to make sure AWS access is working ok (via console and CLI) to be able to show how to create queues, send messages to them etc

## Session

- Run the presentation
- Python Queue demo solution is available in the `solutions/queue_demo.py`
- **Don't** make a demo file called `queue.py`, that will clash with python built in functions by name and give you weird errors!
