import sys
import time

# 打印消息，类似print，但是不会换行（print实际是调用此方法，只是默认会换行而已）
sys.stdout.write('abcde')
sys.stdout.write('fghijk')
sys.stdout.write('\rAAAA')  # \r回到行首，覆盖原来的内容

# 重定向输出，输出到一个文件
temp = sys.stdout  # 暂时保存stdout对象，以便恢复打印到屏幕
sys.stdout=open('a.txt','a')
sys.stdout.write('ccc')
print('aaa')
sys.stdout = temp #恢复默认的stdout，打印到屏幕
print('bbb')

# 打印进度条
n = 0.01
while n<=100:
    sys.stdout.write('\r%s %0.2f%%'%(('*'*round(n/5)).ljust(20,'-'),n))
    sys.stdout.flush()  # 文件打印或者写入等，都不是立刻执行，而是先写入缓存区，flush的作用是强制刷新缓存，实现立刻打印或写入
    time.sleep(0.01)
    n+=0.01

print('\n=============')
x = input('input:')  # input默认输入的数据末尾没有\n
y = sys.stdin.readline()  # 默认末尾会有\n
print(x,end='')    # 设置了不换行，继续打印'X',结果是x+'X'
print('X')
print('---------')
print(y,end='')   # 设置了不换行，继续打印'Y'，结果却换行了，说明y默认的就带有一个换行符
print('Y')




sys.argv           #命令行参数List，第一个元素是程序本身路径
sys.exit(1)        #退出程序，正常退出时exit(0)
sys.version        #获取Python解释程序的版本信息
sys.maxint         #最大的Int值
sys.path           #返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform       #返回操作系统平台名称