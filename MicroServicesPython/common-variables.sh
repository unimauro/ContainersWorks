#!/bin/sh
export profile="demo"
export region="<your-aws-region>"
export aws_account_id=$(aws sts get-caller-identity --query 'Account' --profile $profile | tr -d '\"')
# export aws_account_id="<your-aws-accountid>"
export template="lambda-dynamo-data-api"
export bucket="<you-bucket-name>"
export prefix="tmp/sam"

# Lambda settings
export zip_file="lambda-dynamo-data-api.zip"
export files="lambda_return_dynamo_records.py"
i
