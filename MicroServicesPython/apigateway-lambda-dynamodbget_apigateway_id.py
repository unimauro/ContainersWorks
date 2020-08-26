import argparse
import logging

import boto3
logging.getLogger('botocore').setLevel(logging.CRITICAL)

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(levelname)s %(name)-15s: %(lineno)d %(message)s',
                    level=logging.INFO)
logger.setLevel(logging.INFO)


def get_apigateway_id(endpoint_name):
    client = boto3.client(service_name='apigateway',
             region_name='eu-west-1')
    apis = client.get_rest_apis()
    for api in apis['items']:
        if api['name'] == endpoint_name:
            return api['id']
    return None

def main():
    endpoint_name = "lambda-dynamo-xray"

    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--endpointname", type=str,
                        required=False, help="Path to the endpoint_id")
    args = parser.parse_args()

    if (args.endpointname is not None): endpoint_name = args.endpointname


    apigateway_id = get_apigateway_id(endpoint_name)
    if apigateway_id is not None:
        print(apigateway_id)
        return 0
    else:
        return 1

if __name__ == '__main__':
    main()
