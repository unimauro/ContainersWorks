from boto3 import resource

class DynamoRepository:
    def __init__(self, target_dynamo_table, region='eu-west-1'):
        self.dynamodb = resource(service_name='dynamodb', region_name=region)
        self.target_dynamo_table = target_dynamo_table
        self.table = self.dynamodb.Table(self.target_dynamo_table)     

    def update_dynamo_event_counter(self, event_name, 
        event_datetime, event_count=1):
        response = self.table.update_item(
            Key={
                'EventId': str(event_name),
                'EventDay': int(event_datetime)
            },
            ExpressionAttributeValues={":eventCount": 
                int(event_count)},
            UpdateExpression="ADD EventCount :eventCount")
        return response

######
import csv
table_name = 'user-visits-sam'
input_data_path = '../sample_data/dynamodb-sample-data.txt'
dynamo_repo = DynamoRepository(table_name)
with open(input_data_path, 'r') as sample_file:
    csv_reader = csv.DictReader(sample_file)
    for row in csv_reader:
        response = dynamo_repo.update_dynamo_event_counter(row['EventId'],                                                            row['EventDay'],                                                            row['EventCount'])
        print(response)

