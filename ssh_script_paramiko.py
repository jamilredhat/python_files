import paramiko

remote_host = "192.168.1.201"
ssh_port = 22
ssh_user = "admin"
command = "df -h | grep sd"

ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_connection.connect(remote_host, ssh_port, ssh_user, password="root12")
stdin, stdout, stderr = ssh_connection.exec_command(command)
who_output = stdout.readlines()

for partition in who_output:
    print(partition)
