import logging
from rdsutils import rds_utils
from secgrouputils import security_utils
import config


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

aws_secret_key_id = config.aws_access_key_id
aws_secret_access_key = config.aws_secret_access_key
aws_region_name = config.aws_region_name
dbconfig = config.db_instance
secconfig = config.security

def Configure_RDS(config, groupIds):

    logger.info('Starting RDS Creations')
    rds_object = rds_utils(aws_access_key_id=aws_secret_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region_name)
    result = rds_object.create_dbinstance(dbconfig, groupIds)
    logger.info(result)

def Configure_Security(config):

    logger.info('Starting RDS Creations')
    sec_object = security_utils(aws_access_key_id=aws_secret_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region_name)
    groupResult, groupId = sec_object.Create_Sec_Groups(secconfig['Sec_Groups'])
    logger.info(groupResult)
    if groupId:
        for g in groupId:
            ruleResult = sec_object.Create_Rule(secconfig['Sec_Rules'], g)
    
    logger.info(ruleResult)
    return groupId


test_object = rds_utils(aws_access_key_id=aws_secret_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region_name)
rdsinstances = test_object.get_instances()

for r in rdsinstances['DBInstances']:
    logger.info('Instance Indetifier : {0}' .format(r['DBInstanceIdentifier']))

dbsecgroups = test_object.get_dbsecgroups()
for r in dbsecgroups['DBSecurityGroups']:
    logger.info('DB Security Groups : {0}'.format(r['DBSecurityGroupName']))

secgroupIds = Configure_Security(dbconfig)
print('Security Groups Created')
Configure_RDS(dbconfig, secgroupIds)
print('RDS Created')