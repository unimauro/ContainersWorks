#!/bin/sh
. ./common-variables.sh
rm outputfile.tmp
status_code=$(aws lambda invoke --invocation-type RequestResponse \
    --function-name ${template}-sam --region ${region} \
    --payload file://../../sample_data/request-api-gateway-get-valid.json \
    outputfile.tmp --profile ${profile})
echo "$status_code"
if echo "$status_code" | grep -q "200";
then
    cat outputfile.tmp
    if grep -q error outputfile.tmp;
    then
        echo "\nerror in response"
        exit 1
    else
        echo "\npass"
        exit 0
    fi
else
    echo "\nerror status not 200"
    exit 1
fi
