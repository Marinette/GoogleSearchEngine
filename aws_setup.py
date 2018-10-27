import boto.ec2
import time

def get_key(conn):

    """ Try creating a new key_pair. If key_pair already exits, there will be
        an error. """

    try:
        key_pair = conn.create_key_pair('my_key')
        key_pair.save("")
    # if there is an error (key_pair already exits), get existing key_pair
    except boto.exception.EC2ResponseError:
        key_pair = 'my_key'

    return key_pair

def get_security_group(conn):

    """ Try creating a new security group. If security group already exits,
        there will be an error. """

    try:
        security_group = conn.create_security_group('csc326-group24',
                        'security group for csc326')
        security_group.authorize('icmp', -1, -1, '0.0.0.0/0')
        security_group.authorize('tcp', 22, 22, '0.0.0.0/0')
        security_group.authorize('tcp', 80, 80, '0.0.0.0/0')
        #security_group.authorize('tcp', 8080, 8080, '0.0.0.0/0')
        
    # if there is an error, get existing security group
    except boto.exception.EC2ResponseError:
        security_group = 'csc326-group24'

    return security_group

def aws_setup():

    """ This function connects to us-east-1, sets up an instance,
        copys files to the instance, and starts the server. """

    aws_access_key_id = 'xxxxxxxx'
    aws_secret_access_key = 'xxxxxxxx'
    ami = 'ami-9aaa1cf2'

    # setup connection
    conn = boto.ec2.connect_to_region('us-east-1', aws_access_key_id =
        aws_access_key_id, aws_secret_access_key = aws_secret_access_key)

    key_pair = get_key(conn)

    security_group = get_security_group(conn)

    # start instance
    resp = conn.run_instances(
        ami, instance_type = 't2.micro', key_name = 'my_key',
        security_groups = ['csc326-group24'])

    inst = resp.instances[0]

    while inst.update() != 'running':
        time.sleep(1)

    # get ip address
    address = conn.allocate_address()
    address.associate(inst.id)
    ip = address.public_ip
    print ('The public ip address is ', ip)



aws_setup()
