from unittest import mock

     mock.patch.object(lambda_query_dynamo.DynamoRepository,
                      "query_by_partition_key",
                       return_value=['item'])
     def test_validid_checkstatus_status200(self, 
         mock_query_by_partition_key):
        result = lambda_query_dynamo.Controller.get_dynamodb_records(
                 self.validJsonDataNoStartDate)
        assert result['statusCode'] == '200'

    @mock.patch.object(lambda_query_dynamo.DynamoRepository,
                       "query_by_partition_key",
                        return_value=['item'])
     def test_validid_getrecord_validparamcall(self, 
         mock_query_by_partition_key):         
lambda_query_dynamo.Controller.get_dynamodb_records(
self.validJsonDataNoStartDate)         mock_query_by_partition_key.assert_called_with(
     partition_key='EventId',                                                                      
     partition_value=u'324')

    @mock.patch.object(lambda_query_dynamo.DynamoRepository,
                       "query_by_partition_and_sort_key",
                        return_value=['item'])
    def test_validid_getrecorddate_validparamcall(self, 
        mock_query_by_partition_and_sort_key):
        lambda_query_dynamo.Controller.get_dynamodb_records(
               self.validJsonDataStartDate)
          mock_query_by_partition_and_sort_key.assert_called_with(partition_key='
    EventId',
    partition_value=u'324',
    sort_key='EventDay',
    sort_value=20171013)
