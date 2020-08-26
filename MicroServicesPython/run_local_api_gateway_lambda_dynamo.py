import json

from lambda_dynamo_read import lambda_return_dynamo_records as lambda_query_dynamo

with open('../sample_data/request-api-gateway-valid-date.json', 'r') as sample_file:
     event = json.loads(sample_file.read())
print("lambda_query_dynamo\nUsing data: %s" % event)
print(sample_file.name.split('/')[-1]) response = lambda_query_dynamo.lambda_handler(event, None)
print('Response: %s\n' % json.dumps(response))

