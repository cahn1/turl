#!/bin/bash
aws apigateway create-rest-api --name turl
#{
#    "id": "qpgds5ptla",
#    "name": "turl",
#    "createdDate": 1516605003,
#    "apiKeySource": "HEADER",
#    "endpointConfiguration": {
#        "types": [
#            "EDGE"
#        ]
#    }
#}

aws apigateway get-resources --rest-api-id qpgds5ptla
#{
#    "items": [
#        {
#            "id": "h1r6njqeof",
#            "path": "/"
#        }
#    ]
#}

aws apigateway create-resource --rest-api-id qpgds5ptla --parent-id h1r6njqeof --path-part api
#{
#    "id": "xu49c0",
#    "parentId": "h1r6njqeof",
#    "pathPart": "api",
#    "path": "/api"
#}

aws apigateway create-resource --rest-api-id qpgds5ptla --parent-id xu49c0 --path-part q
#{
#    "id": "5cj2rv",
#    "parentId": "xu49c0",
#    "pathPart": "q",
#    "path": "/api/q"
#}


##
## POST
##

aws apigateway put-method --rest-api-id qpgds5ptla --resource-id 5cj2rv --http-method POST --authorization-type NONE
#{
#    "apiKeyRequired": false,
#    "httpMethod": "POST",
#    "authorizationType": "NONE"
#}
aws apigateway put-integration --rest-api-id qpgds5ptla --resource-id 5cj2rv --http-method POST --type AWS_PROXY --integration-http-method POST --uri  arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:519197270331:function:turl_turl/invocations
#{
#    "type": "AWS_PROXY",
#    "httpMethod": "POST",
#    "uri": "arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:519197270331:function:turl_turl/invocations",
#    "passthroughBehavior": "WHEN_NO_MATCH",
#    "timeoutInMillis": 29000,
#    "cacheNamespace": "5cj2rv",
#    "cacheKeyParameters": []
#}

aws apigateway put-method-response --rest-api-id qpgds5ptla --resource-id 5cj2rv --http-method POST --status-code 200 --response-models "{\"application/json\": \"Empty\"}"
#{
#    "statusCode": "200",
#    "responseModels": {
#        "application/json": "Empty"
#    }
#}

aws apigateway create-deployment --rest-api-id qpgds5ptla --stage-name dev
#{
#    "id": "zt7ewy",
#    "createdDate": 1516671465
#}

aws lambda add-permission --function-name turl_turl \
  --statement-id turl-dev-api1 \
  --action lambda:InvokeFunction \
  --principal apigateway.amazonaws.com \
  --source-arn "arn:aws:execute-api:us-west-2:519197270331:qpgds5ptla/*/POST/api/q"
#  {
#      "Statement": "{\"Sid\":\"turl-dev-api1\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"apigateway.amazonaws.com\"},\"Action\":\"lambda:InvokeFunction\",\"Resource\":\"arn:aws:lambda:us-west-2:519197270331:function:turl_turl\",\"Condition\":{\"ArnLike\":{\"AWS:SourceArn\":\"arn:aws:execute-api:us-west-2:519197270331:qpgds5ptla/*/POST/api/q\"}}}"
#  }
aws apigateway test-invoke-method \
--rest-api-id qpgds5ptla \
--resource-id 5cj2rv \
--http-method POST \
--path-with-query-string "" \
--headers {} \
--body "{\"url\": \"test-url\"}"
#{
#    "status": 200,
#    "body": "",
#    "log": "Execution log for request test-request\nMon Oct 23 07:18:43 UTC 2017 : Starting execution for request: test-invoke-request\nMon Oct 23 07:18:43 UTC 2017 : HTTP Method: POST, Resource Path: /api/q\nMon Oct 23 07:18:43 UTC 2017 : Method request path: {}\nMon Oct 23 07:18:43 UTC 2017 : Method request query string: {}\nMon Oct 23 07:18:43 UTC 2017 : Method request headers: {}\nMon Oct 23 07:18:43 UTC 2017 : Method request body before transformations: {\"station_id\": \"301\", \"status\": \"rain\"}\nMon Oct 23 07:18:43 UTC 2017 : Endpoint request URI: https://lambda.us-west-2.amazonaws.com/2015-03-31/functions/arn:aws:lambda:us-west-2:413035961530:function:ingestor_ingestor/invocations\nMon Oct 23 07:18:43 UTC 2017 : Endpoint request headers: {x-amzn-lambda-integration-tag=test-request, Authorization=************************************************************************************************************************************************************************************************************************************************************************************************************************9e9334, X-Amz-Date=20171023T071843Z, x-amzn-apigateway-api-id=ezj94zbo6b, X-Amz-Source-Arn=arn:aws:execute-api:us-west-2:413035961530:ezj94zbo6b/null/POST/api/q, Accept=application/json, User-Agent=AmazonAPIGateway_ezj94zbo6b, X-Amz-Security-Token=FQoDYXdzEBAaDN1lszO7nRFt7YWKZCK3A2dzmgP4CsqX56pjwOwe8POrEmIGIsPoMxr32GVkpF4hvxDjzatyvadpjcqSQono1cwwfg3CRIpKTVpOntg1P+18puT9e/hNrozyaDw+nQ2/kZtPWef0CjPscuMljKwc+geUhjzu29dl27m1n9PJBm3c0aoyVjCb59N28yiXc2kG9hJ9HCSE1aB6l3O1HJuuHf7dWOoJqEdlWqTfY6E6frJcMsfKbbrf40st2gj3Kb7YX5hAewZaTc8v7OwYlEroSlz1WxG6kx5Zq4zdTlgUnBcOJ3iOaOxTCM0gFpK4UBk+vn7lIPngLSjgl026NEvMf4pKd3vTsQeVtExyR0S4TcujoAA [TRUNCATED]\nMon Oct 23 07:18:43 UTC 2017 : Endpoint request body after transformations: {\"resource\":\"/api/q\",\"path\":\"/api/q\",\"httpMethod\":\"POST\",\"headers\":null,\"queryStringParameters\":null,\"pathParameters\":null,\"stageVariables\":null,\"requestContext\":{\"path\":\"/api/q\",\"accountId\":\"413035961530\",\"resourceId\":\"7hbold\",\"stage\":\"test-invoke-stage\",\"requestId\":\"test-invoke-request\",\"identity\":{\"cognitoIdentityPoolId\":null,\"accountId\":\"413035961530\",\"cognitoIdentityId\":null,\"caller\":\"AIDAJV6CVOAF3DE4BLGS2\",\"apiKey\":\"test-invoke-api-key\",\"sourceIp\":\"test-invoke-source-ip\",\"accessKey\":\"AKIAJKR6KEMPNRXOHTHA\",\"cognitoAuthenticationType\":null,\"cognitoAuthenticationProvider\":null,\"userArn\":\"arn:aws:iam::413035961530:user/cahn\",\"userAgent\":\"aws-cli/1.11.170 Python/2.7.10 Darwin/17.0.0 botocore/1.7.28\",\"user\":\"AIDAJV6CVOAF3DE4BLGS2\"},\"resourcePath\":\"/api/q\",\"httpMethod\":\"POST\",\"apiId\":\"ezj94zbo6b\"},\"body\":\"{\\\"station_id\\\": \\\"301\\\", \\\"status\\\": \\\"rain\\\"}\",\"isBase64Encoded\":false}\nMon Oct 23 07:18:43 UTC 2017 : Sending request to https://lambda.us-west-2.amazonaws.com/2015-03-31/functions/arn:aws:lambda:us-west-2:413035961530:function:ingestor_ingestor/invocations\nMon Oct 23 07:18:44 UTC 2017 : Received response. Integration latency: 943 ms\nMon Oct 23 07:18:44 UTC 2017 : Endpoint response body before transformations: {\"body\": \"\", \"headers\": {}, \"statusCode\": 200}\nMon Oct 23 07:18:44 UTC 2017 : Endpoint response headers: {x-amzn-Remapped-Content-Length=0, Connection=keep-alive, x-amzn-RequestId=66b0cab0-b7c2-11e7-a520-e5c9464d8491, Content-Length=46, Date=Mon, 23 Oct 2017 07:18:44 GMT, X-Amzn-Trace-Id=root=1-59ed97d3-9a51e3ee6e88fb8f24e11e82;sampled=0, Content-Type=application/json}\nMon Oct 23 07:18:44 UTC 2017 : Method response body after transformations: \nMon Oct 23 07:18:44 UTC 2017 : Method response headers: {X-Amzn-Trace-Id=sampled=0;root=1-59ed97d3-9a51e3ee6e88fb8f24e11e82}\nMon Oct 23 07:18:44 UTC 2017 : Successfully completed execution\nMon Oct 23 07:18:44 UTC 2017 : Method completed with status: 200\n",
#    "latency": 957,
#    "headers": {
#        "X-Amzn-Trace-Id": "sampled=0;root=1-59ed97d3-9a51e3ee6e88fb8f24e11e82"
#    }
#}

##
## POST TEST - Provide correct json format
##
#aws apigateway test-invoke-method --rest-api-id qpgds5ptla --resource-id 5cj2rv --http-method POST --path-with-query-string "" --headers {} --body "{\"url\": \"http://dongkuk.tistory.com/entry/Ruby-TDD-Rspec-10%EB%8B%A8%EA%B3%84-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC\?category\=617534\"}"
aws apigateway test-invoke-method --rest-api-id qpgds5ptla --resource-id 5cj2rv --http-method POST --path-with-query-string "" --headers {} --body '{"url": "http://dongkuk.tistory.com/entry/Ruby-TDD-Rspec-10%EB%8B%A8%EA%B3%84-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC\?category\=617534"}'

curl https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q -H "Content-Type: application/json" -X POST -d '{"url":"http://dongkuk.tistory.com/entry/Ruby-TDD-Rspec-10%EB%8B%A8%EA%B3%84-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC\?category\=617534"}'

##
## GET
##
aws apigateway put-method --rest-api-id qpgds5ptla --resource-id 5cj2rv --http-method GET --authorization-type NONE --no-api-key-required --request-parameters { }
#{
#    "httpMethod": "GET",
#    "authorizationType": "NONE",
#    "apiKeyRequired": false
#}

aws apigateway put-integration --rest-api-id qpgds5ptla --resource-id 5cj2rv --http-method GET --type AWS_PROXY --integration-http-method POST --uri  arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:519197270331:function:turl_turl/invocations
#{
#    "type": "AWS_PROXY",
#    "httpMethod": "POST",
#    "uri": "arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:519197270331:function:turl_turl/invocations",
#    "passthroughBehavior": "WHEN_NO_MATCH",
#    "timeoutInMillis": 29000,
#    "cacheNamespace": "5cj2rv",
#    "cacheKeyParameters": []
#}

aws apigateway put-method-response --rest-api-id qpgds5ptla --resource-id 5cj2rv --http-method GET --status-code 200 --response-models "{\"application/json\": \"Empty\"}"
#{
#    "responseModels": {
#        "application/json": "Empty"
#    },
#    "statusCode": "200"
#}
aws apigateway create-deployment --rest-api-id qpgds5ptla --stage-name dev
#{
#    "id": "6dbzy3",
#    "createdDate": 1516745253
#}

aws lambda add-permission --function-name turl_turl \
--statement-id turl-dev-api2 \
--action lambda:InvokeFunction \
--principal apigateway.amazonaws.com \
--source-arn "arn:aws:execute-api:us-west-2:519197270331:qpgds5ptla/*/GET/api/q"
#{
#    "Statement": "{\"Sid\":\"turl-dev-api2\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"apigateway.amazonaws.com\"},\"Action\":\"lambda:InvokeFunction\",\"Resource\":\"arn:aws:lambda:us-west-2:519197270331:function:turl_turl\",\"Condition\":{\"ArnLike\":{\"AWS:SourceArn\":\"arn:aws:execute-api:us-west-2:519197270331:qpgds5ptla/*/GET/api/q\"}}}"
#}


#aws apigateway test-invoke-method --rest-api-id qpgds5ptla --resource-id 5cj2rv --http-method GET --path-with-query-string "short_url=21sN3" --headers {} --body ""
#aws apigateway test-invoke-method --rest-api-id qpgds5ptla --resource-id 5cj2rv --http-method GET --path-with-query-string "{?\"short_url\"=\"21sN3\"}" --headers {} --body ""
#aws apigateway test-invoke-method --rest-api-id qpgds5ptla --resource-id 5cj2rv --http-method GET --path-with-query-string "{?short_url=21sN3}" --headers {} --body ""
aws apigateway test-invoke-method --rest-api-id qpgds5ptla --resource-id 5cj2rv --http-method GET --path-with-query-string "?short_url=21sN3" --headers {} --body ""
curl https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q\?short_url\=21sN3
Postman - https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q?short_url=21sN3



#
# POST, GET test results
#

# GET
curl https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q\?short_url\=21sMz
{"url":"http://dongkuk.tistory.com/entry/Ruby-TDD-Rspec-10%EB%8B%A8%EA%B3%84-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC\\?category\\=617534"}%
aws apigateway test-invoke-method --rest-api-id qpgds5ptla --resource-id 5cj2rv --http-method GET --path-with-query-string "?short_url=21sMz" --headers {} --body ""


curl https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q\?short_url\=21sN1
{"url": "https://www.google.com/search\\?source\\=hp\\&ei\\=ecxmWrnoM9DUjwP1lIvYBg\\&q\\=jump+to+the+python\\&oq\\=jump+to+the+python\\&gs_l\\=psy-ab.3..0i22i30k1.1837.10509.0.10655.35.23.4.1.1.0.657.2582.0j2j2j2j1j1.8.0....0...1c.1.64.psy-ab..22.13.2606...0j46j0i131k1j0i46k1.0.H5eRj6d-nKY"}%
aws apigateway test-invoke-method --rest-api-id qpgds5ptla --resource-id 5cj2rv --http-method GET --path-with-query-string "?short_url=21sN1" --headers {} --body ""

# POST - new_url
curl https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q -H "Content-Type: application/json" -X POST -d '{"url":"https://www.worksheetworks.com/math/multi-digit-operations/division/two-with-three-digit-remainders.html"}'
{"short_url": "21sNs"}%

# POST - existing url
curl https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q -H "Content-Type: application/json" -X POST -d '{"url":"https://shop.scholastic.com/parent-ecommerce/books/james-and-the-giant-peach-9780142410363.html"}'
{"short_url": "21sNA"}%


# Test POST 
curl https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q -H "Content-Type: application/json" -X POST -d '{"url":"https://shop.scholastic.com/parent-ecommerce/books/zac-and-the-dream-stealers-9780545401067.html"}'
curl https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q -H "Content-Type: application/json" -X POST -d '{"url":"http://money.cnn.com/2018/01/26/news/economy/northeast-corridor/index.html"}'
curl https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q -H "Content-Type: application/json" -X POST -d '{"url":"http://dongkuk.tistory.com/entry/Ruby-TDD-Rspec-10%EB%8B%A8%EA%B3%84-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC\?category\=617534"}'
curl https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q -H "Content-Type: application/json" -X POST -d '{"url":"https://nec.amtrak.com/news/gateway-program-development-corporation-releases-request-for-information-for-hudson-tunnel-project/"}'
curl https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q -H "Content-Type: application/json" -X POST -d '{"url":"http://boto3.readthedocs.io/en/latest/reference/services/dynamodb.html\#DynamoDB.Table.put_item"}'
curl https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q -H "Content-Type: application/json" -X POST -d '{"url":"https://shop.scholastic.com/parent-ecommerce/books/wonder-9780375869020.html"}'
curl https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q -H "Content-Type: application/json" -X POST -d '{"url":"https://disneyland.disney.go.com/faq/tickets/eticket-terms-conditions/"}'
curl https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q -H "Content-Type: application/json" -X POST -d '{"url":"https://www.google.com/search\?source\=hp\&ei\=ecxmWrnoM9DUjwP1lIvYBg\&q\=jump+to+the+python\&oq\=jump+to+the+python\&gs_l\=psy-ab.3..0i22i30k1.1837.10509.0.10655.35.23.4.1.1.0.657.2582.0j2j2j2j1j1.8.0....0...1c.1.64.psy-ab..22.13.2606...0j46j0i131k1j0i46k1.0.H5eRj6d-nKY"}'
curl https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q -H "Content-Type: application/json" -X POST -d '{"url":"https://shop.scholastic.com/parent-ecommerce/books/james-and-the-giant-peach-9780142410363.html"}'
curl https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q -H "Content-Type: application/json" -X POST -d '{"url":"https://www.worksheetworks.com/math/multi-digit-operations/division/two-with-three-digit-remainders.html"}'
curl https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q -H "Content-Type: application/json" -X POST -d '{"url":"https://shop.scholastic.com/parent-ecommerce/featured-shops/books-by-grade/3rd-grade-books.html"}'
curl https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q -H "Content-Type: application/json" -X POST -d '{"url":"64ff6f9c0327ec9c59db5c31107ed507c36536c9"}'
curl https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q -H "Content-Type: application/json" -X POST -d '{"url":"http://category.gmarket.co.kr/listview/List.aspx\?gdmc_cd\=200002017"}'
curl https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q -H "Content-Type: application/json" -X POST -d '{"url":"http://http://www.example123z.com/"}'
