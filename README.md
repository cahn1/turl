# turl

[![Build Status](http://rango-elb143-elb-lo8yagpknu2v-199439260.us-west-2.elb.amazonaws.com:8080/buildStatus/icon?job=turl_dev)](http://rango-elb143-elb-lo8yagpknu2v-199439260.us-west-2.elb.amazonaws.com:8080/job/turl_dev/lastBuild/console)

Simple Application for Shortening URLs

## Sample Usage

**POST** - Generate short url or retrieve if exists

```
curl APIGW_URL -H "Content-Type: application/json" -X POST -d '{"url":"LONG_URL"}'
```

```
aws apigateway test-invoke-method --rest-api-id qpgds5ptla --resource-id 5cj2rv --http-method POST --path-with-query-string "" --headers {} --body '{"url": "LONG_URL"}'
```

For example:

```
curl https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q -H "Content-Type: application/json" -X POST -d '{"url":"https://shop.scholastic.com/parent-ecommerce/books/zac-and-the-dream-stealers-9780545401067.html"}'
```

```
aws apigateway test-invoke-method --rest-api-id qpgds5ptla --resource-id 5cj2rv --http-method POST --path-with-query-string "" --headers {} --body '{"url": "http://money.cnn.com/2018/01/26/news/economy/northeast-corridor/index.html"}'

{
    "status": 200,
    "body": "{\"short_url\": \"21sNA\"}",
    "headers": {
        "X-Amzn-Trace-Id": "sampled=0;root=1-5a6c2833-0d5ae1e8f2a2cb0e0e95731a"
    },
    "log": "Execution log for request test-request\nSat Jan 27 07:20:19 UTC 2018 : Starting execution for request: test-invoke-request\nSat Jan 27 07:20:19 UTC 2018 : HTTP Method: POST, Resource Path: /api/q\nSat Jan 27 07:20:19 UTC 2018 : Method request path: {}\nSat Jan 27 07:20:19 UTC 2018 : Method request query string: {}\nSat Jan 27 07:20:19 UTC 2018 : Method request headers: {}\nSat Jan 27 07:20:19 UTC 2018 : Method request body before transformations: {\"url\": \"http://money.cnn.com/2018/01/26/news/economy/northeast-corridor/index.html\"}\nSat Jan 27 07:20:19 UTC 2018 : Endpoint request URI: https://lambda.us-west-2.amazonaws.com/2015-03-31/functions/arn:aws:lambda:us-west-2:519197270331:function:turl_turl/invocations\nSat Jan 27 07:20:19 UTC 2018 : Endpoint request headers: {x-amzn-lambda-integration-tag=test-request, Authorization=************************************************************************************************************************************************************************************************************************************************************************************************************************60059b, X-Amz-Date=20180127T072019Z, x-amzn-apigateway-api-id=qpgds5ptla, X-Amz-Source-Arn=arn:aws:execute-api:us-west-2:519197270331:qpgds5ptla/null/POST/api/q, Accept=application/json, User-Agent=AmazonAPIGateway_qpgds5ptla, X-Amz-Security-Token=FQoDYXdzEJ///////////wEaDBuwABDnJuIAi1t6gCK3A/lwoLmsyhugnZZsj4nlubXw44RSFDDIGY27JIfYj6XuHZ7KvSJqGQGTDdKep0t4zp+5N/6GC8kWQ8lbH6HzLdGcj94zzaKybnz8QkoyoK9kLtq9Ofj+zdksh68VYdAf0zc7+aljxTyho8qLxke6KjviZl/U0HZmjj0i2eeFfelhUlDfEBcBkGG+ZMXJszyGetiFmRaoHMQqh1RdIWXAArZpMGYoh1ma+antubSTix/pGterYf8jXx2pWd9jDtKw5/7br42e3xd50ZPUPWklZEfAcuJ3yqJRLCmiNK1JD4732W85lvh40OZzxazbNRKF6mGlE6AjBHYrHi5 [TRUNCATED]\nSat Jan 27 07:20:19 UTC 2018 : Endpoint request body after transformations: {\"resource\":\"/api/q\",\"path\":\"/api/q\",\"httpMethod\":\"POST\",\"headers\":null,\"queryStringParameters\":null,\"pathParameters\":null,\"stageVariables\":null,\"requestContext\":{\"path\":\"/api/q\",\"accountId\":\"519197270331\",\"resourceId\":\"5cj2rv\",\"stage\":\"test-invoke-stage\",\"requestId\":\"test-invoke-request\",\"identity\":{\"cognitoIdentityPoolId\":null,\"cognitoIdentityId\":null,\"apiKey\":\"test-invoke-api-key\",\"cognitoAuthenticationType\":null,\"userArn\":\"arn:aws:iam::519197270331:user/cahn\",\"apiKeyId\":\"test-invoke-api-key-id\",\"userAgent\":\"aws-cli/1.14.30 Python/3.6.4 Darwin/17.3.0 botocore/1.8.34\",\"accountId\":\"519197270331\",\"caller\":\"AIDAI76NF47SQ525DTBKC\",\"sourceIp\":\"test-invoke-source-ip\",\"accessKey\":\"AKIAI56P427HG4RSH3LA\",\"cognitoAuthenticationProvider\":null,\"user\":\"AIDAI76NF47SQ525DTBKC\"},\"resourcePath\":\"/api/q\",\"httpMethod\":\"POST\",\"apiId\":\"qpgds5ptla\"},\"body\":\"{\\\"url\\\": \\\"http://money.cnn.com/2018/01/26/news/economy/northeast-corridor/index.html\\\"}\",\"isBase64Encoded\":false}\nSat Jan 27 07:20:19 UTC 2018 : Sending request to https://lambda.us-west-2.amazonaws.com/2015-03-31/functions/arn:aws:lambda:us-west-2:519197270331:function:turl_turl/invocations\nSat Jan 27 07:20:20 UTC 2018 : Received response. Integration latency: 597 ms\nSat Jan 27 07:20:20 UTC 2018 : Endpoint response body before transformations: {\"body\": \"{\\\"short_url\\\": \\\"21sNA\\\"}\", \"headers\": {}, \"statusCode\": 200}\nSat Jan 27 07:20:20 UTC 2018 : Endpoint response headers: {X-Amz-Executed-Version=$LATEST, x-amzn-Remapped-Content-Length=0, Connection=keep-alive, x-amzn-RequestId=87d9670f-0332-11e8-ab63-7bfd55c2c69c, Content-Length=72, Date=Sat, 27 Jan 2018 07:20:20 GMT, X-Amzn-Trace-Id=root=1-5a6c2833-0d5ae1e8f2a2cb0e0e95731a;sampled=0, Content-Type=application/json}\nSat Jan 27 07:20:20 UTC 2018 : Method response body after transformations: {\"short_url\": \"21sNA\"}\nSat Jan 27 07:20:20 UTC 2018 : Method response headers: {X-Amzn-Trace-Id=sampled=0;root=1-5a6c2833-0d5ae1e8f2a2cb0e0e95731a}\nSat Jan 27 07:20:20 UTC 2018 : Successfully completed execution\nSat Jan 27 07:20:20 UTC 2018 : Method completed with status: 200\n",
    "latency": 618
}
```


**GET** - Retrieve LONG_URL from SHORT_URL

```
curl APIGW_URL\?short_url\=21sMz
```

```
aws apigateway test-invoke-method --rest-api-id qpgds5ptla --resource-id 5cj2rv --http-method GET --path-with-query-string "?short_url=21sN4" --headers {} --body ""
```

For example:

```
curl https://qpgds5ptla.execute-api.us-west-2.amazonaws.com/dev/api/q\?short_url\=21sMz
{"url": "https://shop.scholastic.com/parent-ecommerce/books/zac-and-the-dream-stealers-9780545401067.html"
```

```
aws apigateway test-invoke-method --rest-api-id qpgds5ptla --resource-id 5cj2rv --http-method GET --path-with-query-string "?short_url=SHORT_URL" --headers {} --body ""

{
    "status": 200,
    "body": "{\"url\": \"https://shop.scholastic.com/parent-ecommerce/books/wonder-9780375869020.html\"}",
    "headers": {
        "X-Amzn-Trace-Id": "sampled=0;root=1-5a6c288d-9ff759d48389cd3f4b2e8760"
    },
    "log": "Execution log for request test-request\nSat Jan 27 07:21:49 UTC 2018 : Starting execution for request: test-invoke-request\nSat Jan 27 07:21:49 UTC 2018 : HTTP Method: GET, Resource Path: \nSat Jan 27 07:21:49 UTC 2018 : Method request path: {}\nSat Jan 27 07:21:49 UTC 2018 : Method request query string: {short_url=21sN4}\nSat Jan 27 07:21:49 UTC 2018 : Method request headers: {}\nSat Jan 27 07:21:49 UTC 2018 : Method request body before transformations: \nSat Jan 27 07:21:49 UTC 2018 : Endpoint request URI: https://lambda.us-west-2.amazonaws.com/2015-03-31/functions/arn:aws:lambda:us-west-2:519197270331:function:turl_turl/invocations\nSat Jan 27 07:21:49 UTC 2018 : Endpoint request headers: {x-amzn-lambda-integration-tag=test-request, Authorization=************************************************************************************************************************************************************************************************************************************************************************************************************************6b609e, X-Amz-Date=20180127T072149Z, x-amzn-apigateway-api-id=qpgds5ptla, X-Amz-Source-Arn=arn:aws:execute-api:us-west-2:519197270331:qpgds5ptla/null/GET/api/q, Accept=application/json, User-Agent=AmazonAPIGateway_qpgds5ptla, X-Amz-Security-Token=FQoDYXdzEKD//////////wEaDAtOTHs9EDZQ8Rd+2SK3A+ph74i9gjw7gLy9qfh9zDEu8vL+M8CyjP2UAxqzbric41Mhxl8QYPK1xD0YslwNzk7KYj86CpuFnDgOcAI8OyZ5h2Yjb1gXJZApwxNVIOko1yFxQJIvSr6Tzsa0QcuAVKO5ab4+D+hQs0F0XlbAa2rGpYeaYdQpUbfbb5lChHzscPjwXLRvCTg4bdshOiJc5iON3n2Qvn0V0n97vkeuZWmmH2vRsVR+94BQi8BFDwHdkMPBPfQK5JFJ6BH3SxAASanSYRF2JxhxDdYup6KhyB8r74vLQyBJHmhCn7cLVdEmLVrzDryZf1FdLl16TG242sI1HHHmvK8do2BS [TRUNCATED]\nSat Jan 27 07:21:49 UTC 2018 : Endpoint request body after transformations: {\"resource\":\"/api/q\",\"path\":\"\",\"httpMethod\":\"GET\",\"headers\":null,\"queryStringParameters\":{\"short_url\":\"21sN4\"},\"pathParameters\":null,\"stageVariables\":null,\"requestContext\":{\"path\":\"/api/q\",\"accountId\":\"519197270331\",\"resourceId\":\"5cj2rv\",\"stage\":\"test-invoke-stage\",\"requestId\":\"test-invoke-request\",\"identity\":{\"cognitoIdentityPoolId\":null,\"cognitoIdentityId\":null,\"apiKey\":\"test-invoke-api-key\",\"cognitoAuthenticationType\":null,\"userArn\":\"arn:aws:iam::519197270331:user/cahn\",\"apiKeyId\":\"test-invoke-api-key-id\",\"userAgent\":\"aws-cli/1.14.30 Python/3.6.4 Darwin/17.3.0 botocore/1.8.34\",\"accountId\":\"519197270331\",\"caller\":\"AIDAI76NF47SQ525DTBKC\",\"sourceIp\":\"test-invoke-source-ip\",\"accessKey\":\"AKIAI56P427HG4RSH3LA\",\"cognitoAuthenticationProvider\":null,\"user\":\"AIDAI76NF47SQ525DTBKC\"},\"resourcePath\":\"/api/q\",\"httpMethod\":\"GET\",\"apiId\":\"qpgds5ptla\"},\"body\":null,\"isBase64Encoded\":false}\nSat Jan 27 07:21:49 UTC 2018 : Sending request to https://lambda.us-west-2.amazonaws.com/2015-03-31/functions/arn:aws:lambda:us-west-2:519197270331:function:turl_turl/invocations\nSat Jan 27 07:21:49 UTC 2018 : Received response. Integration latency: 372 ms\nSat Jan 27 07:21:49 UTC 2018 : Endpoint response body before transformations: {\"body\": \"{\\\"url\\\": \\\"https://shop.scholastic.com/parent-ecommerce/books/wonder-9780375869020.html\\\"}\", \"headers\": {}, \"statusCode\": 200}\nSat Jan 27 07:21:49 UTC 2018 : Endpoint response headers: {X-Amz-Executed-Version=$LATEST, x-amzn-Remapped-Content-Length=0, Connection=keep-alive, x-amzn-RequestId=bd48e856-0332-11e8-aef6-23d84bdce6e1, Content-Length=137, Date=Sat, 27 Jan 2018 07:21:49 GMT, X-Amzn-Trace-Id=root=1-5a6c288d-9ff759d48389cd3f4b2e8760;sampled=0, Content-Type=application/json}\nSat Jan 27 07:21:49 UTC 2018 : Method response body after transformations: {\"url\": \"https://shop.scholastic.com/parent-ecommerce/books/wonder-9780375869020.html\"}\nSat Jan 27 07:21:49 UTC 2018 : Method response headers: {X-Amzn-Trace-Id=sampled=0;root=1-5a6c288d-9ff759d48389cd3f4b2e8760}\nSat Jan 27 07:21:49 UTC 2018 : Successfully completed execution\nSat Jan 27 07:21:49 UTC 2018 : Method completed with status: 200\n",
    "latency": 390
}
```

> Flow
```
" Lambdb: turl
" query(curl)  ---->   api gateway     ---->   Lambda#turl    --> GET   --> dynamodb   --> Lambda#turl     ----> dynamodb
"                     + IAM role               + IAM role                                                        + IAM role
"                     (lambda/cloudwatch)       (dynamodb/cloudwatch)                                           (dynamodb/cloudwatch)
"                                                             --> POST  --> dynamodb   --> Lambda#turl
```
```
.
├── README.md
├── backup
├── lambda
│   ├── functions
│   │   └── turl
│   │       ├── backup
│   │       ├── base62
│   │       │   ├── LICENSE
│   │       │   ├── README.rst
│   │       │   ├── base62.py
│   │       │   ├── base62.pyc
│   │       │   ├── build
│   │       │   │   └── lib
│   │       │   │       └── base62.py
│   │       │   ├── setup.py
│   │       │   └── tests
│   │       │       ├── __init__.py
│   │       │       ├── requirements.txt
│   │       │       └── test_basic.py
│   │       ├── main.py
│   │       └── requirements.txt
│   └── project.json
├── sceptre
│   ├── config
│   │   └── dev
│   │       ├── config.yaml
│   │       ├── ddb-dev-url.yaml
│   │       └── turl-lambda-function.yaml
│   └── templates
│       ├── ddb-dev-url.yaml
│       └── turl-lambda-function.yaml
├── scripts
│   ├── create_apigw.py
│   ├── create_apigw.sh
│   ├── dynamodb_initial_item.sh
│   └── lambda_add_permission.sh
└── test-data
    ├── curltest.sh
    ├── data1.json
    ├── data2.json
    ├── flow.bash
    ├── sample_GET.txt
    ├── sample_GET1.txt
    ├── sample_POST.txt
    ├── sample_POST1.txt
    └── sample_POST2.txt

```
