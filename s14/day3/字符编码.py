# python3默认使用utf-8编码
import sys

# 查看当前默认编码
# print(sys.getdefaultencoding())

name = '你好'  # Unicode类型，这是python3默认的类型
name_utf8 = name.encode('utf-8')
name_gbk = name.encode('gbk') # utf-8也是unicode，可以直接编码成其他类型:gbk
print(name_utf8)
print(name_gbk)
print(name_gbk.decode('gbk')) # gbk先按照gbk的格式解码，成Unicode，然后才能编码成其他类型
print(name_gbk.decode('gbk').encode('utf-8'))

'''总结：
1. 想要打开文件不乱码，首先解释器和文件编码要一致，例如本文件在pycharm打开，
   文件用的编码类型是utf-8,pycharm也设置此文件为utf-8类型，
   python首行通常的 #-*- coding:utf-8 -*- 就是这个作用，和解释器保持一致。
2. 任何一种编码格式按照自身编码方式decode以后，得到的都是Unicode，然后才能通过Unicode转成其他编码
   例如一个gbk编码的数据，想要转成utf-8，需要先decode('gbk') 然后 encode('utf-8')
3. 乱码的终极原因：程序或者文件认为的编码和实际编码不符。
4. 说到底，python程序中有三个编码：
        first. 文件编码,文件创建的时候就根据 编辑器的设置 确立了
        Second.解释器编码，如 notepad++ 打开一个文件默认使用的编码
        third. 数据编码的格式。例如在python中，不管你如何声明文件的编码方式，
               注意是文件的编码，如： #-*- coding:utf-8 -*-，文件内部的数据依然是用Unicode编码的！
               它可以直接解码成其他编码格式，它只是一种数据类型而已。
'''