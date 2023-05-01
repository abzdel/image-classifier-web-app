# check if model is inactive
if [[ $(aws sagemaker list-models | jq ".Models[0].ModelName") == null ]]; then
    echo "model inactive. run './summarize deploy' to deploy model and activate the query functionality"
    exit 1
fi

# take command line input - should be name of file
if [[ $# -eq 0 ]]; then
    echo "no input file specified"
else
    export image=$1
fi

# source check_active to ensure we have endpoint & model names in environment
export endpt=$(aws sagemaker list-endpoints | jq ".Endpoints[0].EndpointName")

# pull endpoint name & clean for invoke command
endpt_temp=$(echo $endpt | tr -d '"') # remove quotes for sagemaker invocation


echo "invoking endpoint..."
aws sagemaker-runtime invoke-endpoint \
    --endpoint-name $endpt_temp \
    --body file://$image \
    --content-type image/jpeg \
    --accept application/json \
    result.txt

echo -e "finished, results in result.txt\n"
echo "result: "



exit 0