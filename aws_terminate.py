import boto
import boto.ec2

def aws_terminate():

    """ This function connects to us-east-1 and terminates the instance. """

    instance_ID = 'xxxxxxxx'

    aws_access_key_id = 'xxxxxxxx'
    aws_secret_access_key = 'xxxxxxxx'

    conn = boto.ec2.connect_to_region(
        'us-east-1', aws_access_key_id = aws_access_key_id,
	     aws_secret_access_key = aws_secret_access_key)

    conn.terminate_instances(instance_ids = [instance_ID])

aws_terminate()
