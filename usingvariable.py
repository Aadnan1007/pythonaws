#Libraries required  boto3,cloudpickle

import boto3

def getVarFromFile(filename):
    import cloudpickle
    f = open(filename)
    global data
    data = cloudpickle.load(file,  fix_imports=True, encoding="ASCII", errors="strict")
    f.close()


getVarFromFile('config.properties')

client = boto3.client(
's3',
    aws_access_key_id=data.aws_access_key_id_value,
    aws_secret_access_key=data.aws_secret_access_key_value
)

response = client.create_bucket(
    Bucket='adanl-boto3-test-delete',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-3',
    },
)

print (response)