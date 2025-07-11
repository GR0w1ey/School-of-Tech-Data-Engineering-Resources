# ETL (SoT version with Postgres)

The module expands on previous sessions (like [data-persistence](../data-persistence/), [data-cleansing](../data-cleansing/), [databases-sot](../databases-sot/) and [data-normalisation](../data-normalisation/)) to bring us full circle to write some code that does all the steps - thus - ETL.

The solutions to the exercise are provided with an in-memory example (python code) example and a pure-sql example - see [./solutions/README.md](./solutions/README.md).

If the learners want to do the `T` bit of the `E-T-L` in SQL they can build up from the from the `databases` session with the addition of grouping, aggregating and renaming columns and their contents (e.g. `GROUP BY` , `COUNT`, `AVERAGE`, `SUM` and `AS`).

## Overview

- High level definition of ETL
- What problems can ETL solve?
- What happens in each stage?
- ETL vs ELT

## Timings

- This session is timetabled for 2 blocks at 1.5 hrs each, i.e. 0.5 elapsed training days
- The formative assessments occur during this and are included in that timing
- The exercises for this session (done in breakouts) are also included in that time

Typically, the exposition slides up to the exercise (approx. Slide 35/44) takes about an 1.0-1.5 hrs, depending on how much chit-chat there is.

The exercise is quite long and depending on approach will take about 1.5 hours for many learners - in breakout rooms helping each other is best.

## Assessments

To check the learner progress in this session we have:

- Multiple Quizzes throughout the session with answer walkthrough
- Follow along demo for the students
- Set of exercises are ran in breakout room

## Prep

- Create the session files (pdf and zip) using `make generate-session-files f=module_name`
- Review the slides and exercises
- Familiarise yourself with the above SQL commands and also the use cases for an ETL pipeline
Be ready to demonstrate working code for each of the 'Demo' sections

Needs Docker or Podman running a postgres container that we can use to save the data - see also the [Docker](../docker/) or [databases](../databases/) or [databases-sot](../databases-sot/) sessions.

- The [docker-compose.yml](./handouts/docker-compose.yml) used here is the same as for the above mentioned [databases-sot](../databases-sot/) session.

## Session

- Run the presentation
- Expect to finish the exposition / theory slides after approx. 1.5hrs and have approx 1.5hrs for the exercises
- The exercise(s) are good in breakouts of 3-5 people helping each other / collaborating

### Exercises in the Session

The exercise asks learners to write a Python script that executes an ETL pipeline. This takes a long time - in full, typically 1.5 hrs.

This needs Docker or Podman running. We need an Adminer and Postgres container running, for the exercise code to save the data into.

The full exercise is in three main parts - write Extract code (load a CSV), write Transform code (of the CSV data), and Load (to save the data in Postgres). This is designed to bring together the building-blocks of several previous sessions.

There is also a fourth part to do some analysis of the acquired data.
