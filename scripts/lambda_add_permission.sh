# add trigger(permission) for api gateway to invoke the lambda function
aws lambda add-permission --function-name arn:aws:lambda:us-west-2:519197270331:function:turl_turl --source-arn "arn:aws:execute-api:us-west-2:519197270331:qqlfrb4ca6/*/POST/api/q" --principal apigateway.amazonaws.com --statement-id 88b42004-f504-44d5-9adf-d027ee65a890 --action lambda:InvokeFunction
