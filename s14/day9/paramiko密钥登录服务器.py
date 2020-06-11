import paramiko

private_key = paramiko.RSAKey.from_private_key_file('id_rsa')

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不存在在know_hosts文件里的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='45.78.30.119', port=29370, username='root',pkey=private_key)

# 执行命令
stdin,stdout,stderr = ssh.exec_command('ls')
result = stdout.read()
print(result)

# 关闭连接
ssh.close()






print(f'{"SSH封装Transport":=^50}')
import paramiko

private_key = paramiko.RSAKey.from_private_key_file('id_rsa') # id_rsa是本地私钥，需要服务器配置公钥
transport = paramiko.Transport(('45.78.30.119', 29370))
transport.connect(username='root',pkey=private_key)
# 创建SSH对象
ssh = paramiko.SSHClient()
ssh._transport = transport
# 执行命令
stdin,stdout,stderr = ssh.exec_command('ls')
result = stdout.read()
print(result)

# 关闭连接
transport.close()