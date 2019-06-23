import boto3
import click

ec2client = boto3.client('ec2')
response = ec2client.describe_instances()

@click.group()
def ec2():
    "listec2 helps wiwth your ec2 instances"
    pass


@ec2.command('list-instances')
def list_instances():
    "List all ec2 instances"
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            # This sample print will output entire Dictionary object
            # print(instance)
            # This will print will output the value of the Dictionary key 'InstanceId'
            print("------------------------------")
            print(instance["InstanceType"])
            print(instance["InstanceId"])
            # print(instance['PublicIpAddress'])
            print(instance['LaunchTime'])
            print(instance['State'])

if __name__ == '__main__':
    ec2()
