import unittest
import json

class TestIndexGetMethod(unittest.TestCase):
    def setUp(self):
        self.validJsonDataNoStartDate = json.loads('{"httpMethod": 
        "GET","path": "/path/to/resource/324","headers": ' \ 'null} ')
        self.validJsonDataStartDate = 
        json.loads('{"queryStringParameters": {"startDate":      
        "20171013"},' \ '"httpMethod": "GET","path": "/path/to/resource
        /324","headers": ' \ 'null} ')
        self.invalidJsonUserIdData =   
        json.loads('{"queryStringParameters": {"startDate": 
        "20171013"},' \ '"httpMethod": "GET","path": "/path/to/resource
        /324f","headers": ' \ 'null} ')
        self.invalidJsonData = "{ invalid JSON request!} "
    def tearDown(self):
        pass
