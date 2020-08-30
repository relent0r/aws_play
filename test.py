dbcreation = {'ResponseMetadata': {
    'RequestId': '123456'
}
}

result = 'RDS Creation Requested Successfully. Request ID is {0}' .format(dbcreation['ResponseMetadata']['RequestId'])
print(result)