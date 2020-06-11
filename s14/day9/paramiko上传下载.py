import paramiko

transport = paramiko.Transport(('45.78.30.119', 29370))
transport.connect(username='root',password='73yCgHhYEs6x')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将id_rsa 上传至服务器并重命名 /tmp/test.py
sftp.put('id_rsa', '/tmp/ras.py')
# ras.py 下载到本地 ras.py
sftp.get('/tmp/ras.py', 'ras.py')

transport.close()


print(f'{"SFTP封装Transport":=^50}')

import paramiko

private_key = paramiko.RSAKey.from_private_key_file('id_rsa') # id_rsa是本地的私钥，需要服务器上配制公钥

transport = paramiko.Transport(('45.78.30.119', 29370))
transport.connect(username='root', pkey=private_key)

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('/tmp/location.py', '/tmp/test.py')
# 将remove_path 下载到本地 local_path
sftp.get('remove_path', 'local_path')

transport.close()