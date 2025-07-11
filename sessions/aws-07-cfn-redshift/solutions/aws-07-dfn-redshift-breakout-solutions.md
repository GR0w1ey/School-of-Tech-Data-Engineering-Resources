# AWS 07 - Intro to Amazon Redshift + Redshift with IaC

> These breakouts work best if the project Teams work on it together (so, breakout per project team).

## Your team name

Your team name will have been provided by the instructors, e.g `la-vida-mocha`. Make sure you used that for the steps below.

## Step 01 - Deploying

- The deployment should work
- The lambda code should be updated

## Step 02 - Trigger lambda

- The lambda should have a successful invocation
- The cloudwatch logs should show the data going into RedShift

## Step 03 - Create SQL Queries

- The team should be able to select the data and work with it in the RedShift query editor console
- Make a query to Display Store name by Rating
    - Some sample SQL could be
        - `SELECT m.store_name, m.overall_score FROM mystery_shop_visit m ORDER BY m.store_name;`
    - And also
        - `SELECT m.store_name, MAX(m.overall_score) AS max_score FROM mystery_shop_visit m GROUP BY m.store_name ORDER BY max_score desc;`
