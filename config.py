
aws_access_key_id = '****'
aws_secret_access_key = '****'
aws_region_name = 'ap-southeast-2'
db_instance = {
    'DBName' : 'awtestdb',
    'DBInstanceIdentifier' : 'aaronwtestdbinstance',
    'AllocatedStorage' : 5,
    'DBInstanceClass' : 'db.t2.micro',
    'Engine' : 'mysql',
    'MasterUsername' : 'wpmaster',
    'MasterUserPassword' : '3VWnOhp96Jk',
    #'VpcSecurityGroupIds' : [
    #    'sg-061f399c4603191a1',
    #],
    'AvailabilityZone' : 'ap-southeast-2b',
    'DBSubnetGroupName' : 'testdbsubnetgroup',
    'Tags':[
        {
            'Key': 'Owner',
            'Value': 'Aaron'
        },
    ],
    'Port' : 3306,
    'EngineVersion' : '8.0.20',
    'EnableIAMDatabaseAuthentication' : True
    

}

security = {
    'Sec_Groups' : [
        {
            'Description' : 'Automated Sec Group',
            'GroupName' : 'EC2 to RDS',
            'VpcId' : 'vpc-0fef482808e038b30',
            'TagSpecifications' : [
                {
                    'ResourceType' : 'security-group',
                    'Tags' : [
                        {
                            'Key' : 'Owner',
                            'Value' : 'Aaron'
                        },
                    ]
                },
            ],
            'DryRun' : False
        },
    ],
    'Sec_Rules' : [
        {
            'Direction' : 'Inbound',
            'DryRun' : False,
            'GroupName' : 'EC2 to RDS',
            'IpPermissions' : [
                {
                    'FromPort' : 3306,
                    'IpProtocol' : 'TCP',
                    'IpRanges' : [
                        {
                            'CidrIp' : '10.12.13.10/32',
                            'Description' : 'Test Automation MySQL'
                        },
                    ],
                    'ToPort' : 3306,
                },
            ]
        },
    ]
}