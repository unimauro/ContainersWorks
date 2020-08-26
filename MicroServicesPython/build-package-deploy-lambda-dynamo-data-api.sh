#!/usr/bin/env bash

# Variables
. ./common-variables.sh

#Create Zip file of your Lambda code (works on Windows and Linux)
./create-lambda-package.sh

#Package your Serverless Stack using SAM + Cloudformation
aws cloudformation package --template-file $template.yaml \
    --output-template-file ../../package/$template-output.yaml \
    --s3-bucket $bucket --s3-prefix backend \
    --region $region --profile $profile

#Deploy your Serverless Stack using SAM + Cloudformation
aws cloudformation deploy --template-file ../../package/$template-output.yaml \
    --stack-name $template --capabilities CAPABILITY_IAM \
    --parameter-overrides AccountId=${aws_account_id} \
    --region $region --profile $profile
