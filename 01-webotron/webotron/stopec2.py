
import boto3


ec2client = boto3.client('ec2')

response = ec2client.stop_instances(
    InstanceIds=[
        'enter instance ID here',
    ],
    Force=True|False
)
