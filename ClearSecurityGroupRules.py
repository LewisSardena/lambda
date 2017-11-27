import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    security_group = ec2.SecurityGroup('sg-2931984f')

    security_group.revoke_ingress(IpPermissions=security_group.ip_permissions)
