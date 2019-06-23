import boto3

ec2client = boto3.client('ec2')
response = ec2client.terminate_instances.all()
#     InstanceIds=[
#         'enter instance id here',
#     ],
# )
