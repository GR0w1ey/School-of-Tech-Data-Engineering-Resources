
aws sqs send-message --queue-url "https://sqs.eu-west-1.amazonaws.com/745580839125/gregor-rowley-coffee-sales-queue" --message-body "Gregor bought a hot chocolate" --profile sot-academy
 

aws sqs send-message --queue-url "https://sqs.eu-west-1.amazonaws.com/745580839125/gregor-rowley-sales-errors-dlq" --message-body "Gregor bought a hot chocolate" --profile sot-academy

aws sns publish --topic-arn "arn:aws:sns:eu-west-1:745580839125:gregor-rowley-coffee-sales-notifications.fifo" --message "Latte for Gregor" --message-group-id "Coffee-Sales" --message-deduplication-id "001"
