# SSHClient 基于用户名和密码连接服务器
import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='45.78.30.119', port=29370, username='root', password='73yCgHhYEs6x')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('ls')
# 获取命令结果
result1 = stdout.read()
result2 = stderr.read()
print(result1,result2,sep='\n')
# 关闭连接
ssh.close()



print(f'{"SSH封装Transport":=^50}')

# SSHClient 封装 Transport，基于用户名和密码连接服务器

import paramiko

transport = paramiko.Transport(('45.78.30.119', 29370))
transport.connect(username='root', password='73yCgHhYEs6x')

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('ls')
print (stdout.read())

transport.close()
