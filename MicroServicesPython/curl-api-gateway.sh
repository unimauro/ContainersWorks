. ./common-variables.sh
endpoint="$(python get_apigateway_endpoint.py -e ${template})"
echo ${endpoint}
status_code=$(curl -i -H \"Accept: application/json\" -H \"Content-Type: application/json\" -X GET ${endpoint})
echo "$status_code"
if echo "$status_code" | grep -q "HTTP/1.1 200 OK";
then
    echo "pass"
    exit 0
else
    exit 1
fi
