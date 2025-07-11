# AWS 07 - Intro to Amazon Redshift + Redshift with IaC

> These breakouts work best if the project Teams work on it together (so, breakout per project team).

## Breakout steps

Now we've seen a demonstration of deploying our Redshift changes, let's run through it in our project groups.

For each breakout room, nominate a driver to screen share their terminal and AWS console view, and then work through the steps below as a group.

## Your team name

Your team name will have been provided by the instructors, e.g `la-vida-mocha` (with dashes `-`).  Make sure you use that for all the steps below.

## Step 01 - Deploying

> Only ONE person should do this with the rest of the team watching
>
> ...have a think about why!

First:

- Log in depending on your AWS login method
    - If on windows, you may need to run the below commands in PowerShell
- Run
    - Either `aws sso login --profile <your-profile-name>`
    - or `aws-azure-login --profile <you-profile-name>`

Then:

- Open a terminal in the [handouts](../handouts/) folder
    - If using Windows this may need to be in GitBash
- Run `./deploy.sh <profile-name> <team-name-with-dashes>` to update the ETL lambda function:
    - e.g. `./deploy.sh sot-academy la-vida-mocha` (lowercase with dashes `-`).
- This:
    - Updates our SSM parameter environment variable via `etl-stack.yml` changes
    - Adds new python code to handle querying the SSM parameter from Parameter Store
    - Adds new python code to connect to the redshift database:
        - Creates our our `mystery_shop_visit` table if it doesn't already exist
        - Inserts our transformed data into the table, now we've removed the mystery shopper name, reformats the visit date and updates the number of store employees to be an integer instead of a string
- Wait until the `deploy.sh` script has finished updating the stack

## Step 02 - Trigger lambda

> Multiple team members can do this concurrently...
>
> ...Why is that?

- Open the `CloudFormation` page in the AWS console and locate your team's stack, e.g `la-vida-mocha-etl-pipeline`
- Find the the `Resources` tab
    - In it, open the link to your S3 `raw-data` bucket, e.g. `la-vida-mocha-shopper-raw-data`
    - Then upload a copy of `mystery_shops_2024-03.csv` from the `handouts/data` folder
- Back the `Resources` tab, click the link to your ETL Lambda, e.g. `la-vida-mocha-shopper-etl-lambda`
- Navigate the lambda user interface to confirm:
    - The new SSM environment variable has been added
    - The lambda code has now been updated to include the redshift logic
    - The lambda was invoked after you dropped the CSV into the `raw-data` bucket
- Open the cloudwatch logs for your lambda and inspect the log output
    - Look for the most recent log stream, and open it
    - Confirm the redshift logic was executed successfully (no errors!)

## Step 03 - Create SQL Queries

Now navigate to the _Amazon Redshift_ web console:

- Click on the running cluster under `Cluster overview` on the main homepage
- Under the `Query data` dropdown on the top right, select `Query in query editor v2`
- There should be a dropdown on the top left named `redshiftcluster-*****`
    - click the three dots on it
    - and select, `Edit connection`, or `Create connection`
- Under `Other ways to connect`, ensure the `Database user name and password` option is selected
- Open the AWS Service Manager console in another browser tab
    - Find the `Parameter Store` in the left bar
    - Navigate to the parameter called `<your-team-name>_redshift_settings` to find your redshift credentials
        - e.g `la_vida_mocha_redshift_settings`
    - You should be able to see your DB name, DB user name and DB password
- Back in the Redshift user interface,
    - Enter the `Database`, `User name` and `Password` values
    - Click `Save`
- Expand the list of databases under the redshift cluster name
    - Click on your DB name
- Expand the list of Tables for your database
- Access your team's table in the list on the left
    - The tables created by your python lambda code can be viewed under `Public > Tables`
    - You can right-click on your table name and choose the menu option "Select table"
- In the main SQL window, have a go at writing and running some sql queries for your `mystery_shop_visit` table,
    - Make sure your team's database is selected in the dropdown at the top next to `redshiftcluster**`.
- Start with `SELECT * FROM mystery_shop_visit;`
- Make a query for "Display Store name by Rating"
    - Some sample SQL could be
        - `SELECT m.store_name, m.overall_score FROM mystery_shop_visit m ORDER BY m.store_name;`
    - And also
        - `SELECT m.store_name, MAX(m.overall_score) AS max_score FROM mystery_shop_visit m GROUP BY m.store_name ORDER BY max_score desc;`

---

### Optional extra task

> In your own project / exercise time, change your code to do a bulk insert with ['execute_values()'](https://www.psycopg.org/docs/extras.html#fast-execution-helpers).

This will be useful for performance in the Team Projects when inserting large amounts of data from multiple files.

You can refer back to the databases session for this.
