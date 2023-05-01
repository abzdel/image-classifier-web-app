export model=$(aws sagemaker list-models | jq ".Models[0].ModelName")
export endpt=$(aws sagemaker list-endpoints | jq ".Endpoints[0].EndpointName")
export endptconfig=$(aws sagemaker list-endpoint-configs | jq ".EndpointConfigs[0].EndpointConfigName")

# if model endpoint and endpoint config are all empty, then no active resources
if [ -z "$model" ] && [ -z "$endpt" ] && [ -z "$endptconfig" ]; then
    echo "no active resources to delete"
    exit 0
fi

# take out quotes from environment variables, store in temp variables
model_temp=$(echo $model | tr -d '"')
endpt_temp=$(echo $endpt | tr -d '"')
endptconfig_temp=$(echo $endptconfig | tr -d '"')


# load in model and endpoint names
echo "deleting resources..."
aws sagemaker delete-model --model-name $model_temp
echo "model deleted"
aws sagemaker delete-endpoint --endpoint-name $endpt_temp
echo "endpoint deleted"
aws sagemaker delete-endpoint-config --endpoint-config-name $endptconfig_temp
echo "endpoint config deleted"

echo "all resources successfully deleted!"


exit 0
#inspect_args # add back if you want to add args or flags