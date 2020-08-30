import boto3
from botocore.exceptions import ClientError
import logging
import config


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

aws_secret_key_id = config.aws_access_key_id
aws_secret_access_key = config.aws_secret_access_key
aws_region_name = config.aws_region_name
boto3_sessionclient = boto3.session.Session(aws_access_key_id=aws_secret_key_id, aws_secret_access_key=aws_secret_access_key,)
services = boto3_sessionclient.get_available_services()
ssm_client = boto3.client('ssm', aws_access_key_id=aws_secret_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region_name)

available_parameters = ssm_client.get_parameter(Name='maxQueryCount')
#for av in available_parameters:

ssm_params = {
    'bakerBoy' : 'James',
    'cakeBoy' : 'Jim',
    'meatBoy' : 'Sam'
}

#for k, v in ssm_params.items():
#    print('Key:'+ k + ' Value :' + v)
#    response = ssm_client.put_parameter(Name=k,
#        Value=v,
#        Type='String',
#        Tags=[
#            {
#                'Key': 'Owner',
#                'Value': 'Aaron'
#            }
#        ]
#    )

executions = ssm_client.get_automation_execution()
if executions:
    for i in executions.items() :
        print(i[0])

print('hi')