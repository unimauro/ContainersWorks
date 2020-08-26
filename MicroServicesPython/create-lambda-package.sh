#!/bin/sh
#setup environment variables
. ./common-variables.sh

#Create Lambda package and exclude the tests to reduce package size
(cd ../../lambda_dynamo_read;
mkdir -p ../package/
zip -FSr ../package/"${zip_file}" ${files} -x *tests/*)

