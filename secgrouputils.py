import boto3
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

class security_utils():

    def __init__(self,aws_access_key_id, aws_secret_access_key, region_name):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.region_name = region_name
        self.sec_client = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

    def Create_Sec_Groups(self, config):
    # Creates security groups based on the config
        response = False
        groupIds = []

        try:
            for s in config:
                response =  self.sec_client.create_security_group(
                    Description=s['Description'],
                    GroupName=s['GroupName'],
                    VpcId=s['VpcId'],
                    TagSpecifications=s['TagSpecifications'],
                    DryRun=s['DryRun']
                )
                if response:
                    logger.info('Response Code is {0}' .format(response['ResponseMetadata']['HTTPStatusCode']))
                    logger.info('Request ID is {0}' .format(response['ResponseMetadata']['RequestId']))
                    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                        result = 'Security group creation requested successfully. Request ID is {0}' .format(response['ResponseMetadata']['RequestId'])
                        groupId = response['GroupId']
                else:
                    result = 'Security group creation failed, see exception data'
                groupIds.append(groupId)
        except ClientError as e:
            logger.info("Unexpected error: {0}"  .format(e))
        
        return result, groupIds

    def Create_Rule(self, config, groupId):
    # Creates rules based on config 
        response = False

        try:
            for s in config:
                if s['Direction'] == 'Inbound':
                    response = self.sec_client.authorize_security_group_ingress(
                        DryRun=s['DryRun'],
                        GroupId=groupId,
                        IpPermissions=s['IpPermissions']
                    )
                elif config['Direction'] == 'Outbound':
                    response = self.sec_client.authorize_security_group_egress(
                        DryRun=s['DryRun'],
                        GroupId=groupId,
                        IpPermissions=s['IpPermissions']
                    )
                else:
                    result = 'Invalid Direction parameter in config'
        except ClientError as e:
            logger.info("Unexpected error: {0}"  .format(e))
        
        if response:
            logger.info('Response Code is {0}' .format(response['ResponseMetadata']['HTTPStatusCode']))
            logger.info('Request ID is {0}' .format(response['ResponseMetadata']['RequestId']))
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                result = 'Rule creation requested successfully. Request ID is {0}' .format(response['ResponseMetadata']['RequestId'])
        else:
            result = 'Rule creation failed, see exception data'

        return result
