import boto3
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

class rds_utils():

    def __init__(self,aws_access_key_id, aws_secret_access_key, region_name):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.region_name = region_name
        self.rds_client = boto3.client('rds', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

        
    def get_instances(self):
        response = self.rds_client.describe_db_instances()
        
        return response
    
    def get_dbsecgroups(self):
        response = self.rds_client.describe_db_security_groups()

        return response

    def create_dbinstance(self, config, sec_groupIds):
    # Creates an RDS instance based on the configuration data
        response = False

        try:
            response = self.rds_client.create_db_instance(
                DBName=config['DBName'],
                DBInstanceIdentifier=config['DBInstanceIdentifier'],
                AllocatedStorage=config['AllocatedStorage'],
                DBInstanceClass=config['DBInstanceClass'],
                Engine=config['Engine'],
                MasterUsername=config['MasterUsername'],
                MasterUserPassword=config['MasterUserPassword'],
                VpcSecurityGroupIds=sec_groupIds,
                AvailabilityZone=config['AvailabilityZone'],
                DBSubnetGroupName=config['DBSubnetGroupName'],
                Port=config['Port'],
                EngineVersion=config['EngineVersion'],
                EnableIAMDatabaseAuthentication=config['EnableIAMDatabaseAuthentication']
    
            )
        except ClientError as e:
            logger.info("Unexpected error: {0}"  .format(e))
        
        if response:
            logger.info('Response Code is {0}' .format(response['ResponseMetadata']['HTTPStatusCode']))
            logger.info('Request ID is {0}' .format(response['ResponseMetadata']['RequestId']))
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                result = 'RDS Creation Requested Successfully. Request ID is {0}' .format(response['ResponseMetadata']['RequestId'])
        else:
            result = 'RDS creation failed, see exception data'

        return result
   
