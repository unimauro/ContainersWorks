import json
      import decimal

      from boto3 import resource
      from boto3.dynamodb.conditions import Key

      class HttpUtils: 
        def init(self):
         pass

      @staticmethod
      def parse_parameters(event):
          try:
              return_parameters = 
              event['queryStringParameters'].copy()
          except Exception:
              return_parameters = {}
          try:
              resource_id = event.get('path', '').split('/')[-1]
              if resource_id.isdigit():
                  return_parameters['resource_id'] = resource_id
              else:
                  return {"parsedParams": None, "err":
                      Exception("resource_id not a number")}
          except Exception as e:
              return {"parsedParams": None, "err": e}  
              # Generally bad idea to expose exceptions
          return {"parsedParams": return_parameters, "err": None}

      @staticmethod
      def respond(err=None, err_code=400, res=None):
          return {
              'statusCode': str(err_code) if err else '200',
              'body': '{"message":%s}' % json.dumps(str(err))
              if err else
              json.dumps(res, cls=DecimalEncoder),
              'headers': {
                  'Content-Type': 'application/json',
                  'Access-Control-Allow-Origin': '*'
              },
          }

      @staticmethod
      def parse_body(event):
          try:
              return {"body": json.loads(event['body']),
                      "err": None}
          except Exception as e:
              return {"body": None, "err": e}

      class DecimalEncoder(json.JSONEncoder): def default(self, o):
      if isinstance(o, decimal.Decimal): if o % 1 > 0:
          return float(o)
      else: return int(o) return super(DecimalEncoder,
          self).default(o)

      class DynamoRepository: def init(self, table_name):
      self.dynamo_client = resource(service_name='dynamodb',
      region_name='eu-west-1') self.table_name =
          table_name self.db_table =
      self.dynamo_client.Table(table_name)

      def query_by_partition_and_sort_key(self,
          partition_key, partition_value,
          sort_key, sort_value):
          response = self.db_table.query(KeyConditionExpression=
                     Key(partition_key).eq(partition_value)
                     & Key(sort_key).gte(sort_value))

          return response.get('Items')

      def query_by_partition_key(self, partition_key,
          partition_value):
          response = self.db_table.query(KeyConditionExpression=
              Key(partition_key).eq(partition_value))
          return response.get('Items')

      def print_exception(e): try: print('Exception %s type' %
              str(type(e))) print('Exception message: %s '
                          % str(e)) except Exception: pass

      class Controller(): def init(self): pass

      @staticmethod
      def get_dynamodb_records(event):
          try:
              validation_result = HttpUtils.parse_parameters(event)
              if validation_result.get(
              'parsedParams', None) is None:
                  return HttpUtils.respond(
                      err=validation_result['err'], err_code=404)
              resource_id = str(validation_result['parsedParams']
                            ["resource_id"])
              if validation_result['parsedParams']
                  .get("startDate") is None:
                  result = repo.query_by_partition_key(
                           partition_key="EventId",
                           partition_value=resource_id)
              else:
                  start_date = int(validation_result['parsedParams']
                               ["startDate"])
                  result = repo.query_by_partition_and_sort_key(
                            partition_key="EventId",
                            partition_value=resource_id,
                            sort_key="EventDay",
                            sort_value=start_date)
                            return HttpUtils.respond(res=result)

                  except Exception as e:
                  print_exception(e)
              return HttpUtils.respond(err=Exception('Not found'),
                  err_code=404)

      table_name = 'user-visits' repo =
                    DynamoRepository(table_name=table_name)

      def lambda_handler(event, context): response =
      Controller.get_dynamodb_records(event) return response
