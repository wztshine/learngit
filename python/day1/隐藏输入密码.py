# Author: zhongtao.wang
import getpass


# can't use in Pycharm.
name = input('name:')
password = getpass.getpass('password:')

print(name,password)