
# PutItem:
curl -X POST -H "Content-Type: application/json" https://qqlfrb4ca6.execute-api.us-west-2.amazonaws.com/dev/api/q -d @data1.json
curl -X POST -H "Content-Type: application/json" https://qqlfrb4ca6.execute-api.us-west-2.amazonaws.com/dev/api/q -d "{\"station_id\":\"095\",\"status\":\"cloudy\",\"timestamp\":\"2017-10-10 17:53\"}" 

# GetItem
curl https://qqlfrb4ca6.execute-api.us-west-2.amazonaws.com/dev/api/q?station_id=091 | jq
