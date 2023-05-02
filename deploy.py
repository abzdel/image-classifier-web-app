from sagemaker.huggingface import HuggingFaceModel
import sagemaker
import os

# role should be codespace secret called AWS_ROLE

role = os.environ['AWS_ROLE']

# Hub Model configuration. https://huggingface.co/models
hub = {
	'HF_MODEL_ID':'microsoft/swin-tiny-patch4-window7-224',
	'HF_TASK':'image-classification'
}

# create Hugging Face Model Class
huggingface_model = HuggingFaceModel(
	transformers_version='4.17.0',
	pytorch_version='1.10.2',
	py_version='py38',
	env=hub,
	role=role, 
)

# deploy model to SageMaker Inference
print('Deploying model to SageMaker Inference')
predictor = huggingface_model.deploy(
	initial_instance_count=1, # number of instances
	instance_type='ml.m5.xlarge' # ec2 instance type
)