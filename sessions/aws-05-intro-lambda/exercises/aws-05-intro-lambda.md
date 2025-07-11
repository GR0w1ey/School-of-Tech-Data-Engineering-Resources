> This is the exercise version of creating a lambda function from scratch code along which can be used for breakout room exercises.

### Part 1 - creating a lambda

- Find the `Lambda` service
- Ensure you are in the correct region `eu-west-1`
- Click on "Create Function"
- Select "Author from scratch"
- Enter a function name e.g. `your-name-de-demo-lambda`
- Select the most recent Python Runtime version you can
    - Notice anything about the available versions?

Notes:
Available Python runtimes in AWS lag behind the most recent releases - it takes AWS time to set them up and test them after Python.org release them. This is the same for all supported Lambda Runtimes (Node, Java, etc).

Adding a Tag called Name makes lots of the AWS (web) Console show us the logical name, which by default, lots of it does not!

---

### Part 1 continued - creating a lambda

- Under `Change default execution role`, select `Use an existing role` and enter `nja-lambda-execution-role`
- Create the function
- Once the function is created, go to the `Configuration` tab and select `Tags` at the side
- Add a new tag with key `Name` and value of the function name

---

### Part 2 - Add event

> Lets have a look at how Events work and logging them.

- Make a new test event with the `Hello-World` template
- Save it for later
- Trigger the Lambda with your test event
- Check the logs in the Lambda page
- Click through to the logs in CloudWatch

A test event in Lambda is a sample input payload used to manually invoke a Lambda function in the AWS Console (typically for testing purposes). It allows you to simulate how your Lambda function would behave when triggered by an actual event source e.g. S3

To create a test event:

- From the Lambda function, go to the "Test" tab
- Enter an event name
- Click 'Save' to save the event
- Click 'Test' to test the event

---

### Part 2 continued - Add event

> Lets log our `event` object.

- Add code to Log (`print()`) the event object
- (Re)deploy the lambda
- Trigger the lambda with your saved Test Event
- Check the CloudWatch logs now have more in them

Remember to always (re)deploy lambda functions when code is updated or changes won't be reflected !

---

### Part 3 - configuration with env vars

> Lets have a look at how Environment Variables ("env vars") work.

- **Never** use these for passwords!
- Using an `.env` file will NOT work here.
- From the lambda function go to 'Configuration' tab
- Select 'Environment variables' on the left hand side
- Click 'Edit' to add a new one
- Add an env var e.g. `FAVOURITE_MOVIE` with a suitable value

In your lambda code:

- Add code to import `os`
- Add code to put the env var in a variable
    - e.g. `fave_movie = os.environ['FAVOURITE_MOVIE']`
- Add code to print the variable
- (Re)deploy the lambda
- Re-Test the lambda and recheck the logs

Env vars can be used for: Feature flags, runtime settings like timeouts or thresholds, handling multi-environment deployments i.e. env variables for dev, prod environments.

---

### Part 4 - updating the return value

> The return value of a Lambda is used to indicate success/failure to the caller, and convey extra information.

- Make a basic Hello message in JSON and return it (sample code is in [./handouts/sample_python_lambda.py](./handouts/sample_python_lambda.py) file.)
- (Re)Deploy the lambda
- Re-Test the lambda
- Check the return value in the logs

Note: there's a difference between returning and printing values in Lambda. Printing values will log the value in CloudWatch logs whereas the value returned will be displayed in the execution status dialogue.

---
