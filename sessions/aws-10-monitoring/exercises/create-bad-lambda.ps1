aws lambda create-function --function-name 'your-name-cafe-monitoring' `
    --zip-file 'fileb://monitoring_lambda.zip' `
    --handler 'lambda_function.lambda_handler' --runtime 'python3.12' `
    --role arn:aws:iam::123456789:role/nja-lambda-execution-role `
    --profile 'sot-academy' --region 'eu-west-1' --timeout 60
