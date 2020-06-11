import sys
import os

# cmd = "dir"
# res = os.popen(cmd) #执行命令
# print(res.read()) # 读取命令行返回信息
# print(sys.argv)  # 是一个列表，第一个元素是本身路径，后面的元素是传递的命令行参数
#
# a,b,c = 1,2,3
# d = 5 if a>b else c
# print(d)
# if a>b:
#     d=5
# else:
#     d=c

msg = '我爱北京天安门'
# encode,编码，把string转成二进制，decode从二进制转成字符串
print(msg.encode(encoding='utf-8').decode(encoding='utf-8'))

# 格式化输出
name = 'Alex'
print('name is {Name}'.format(Name=name))
