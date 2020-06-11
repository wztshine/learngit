import hashlib
import os
import send2trash

'''find the same file in a folder ,
use md5 and sha512 to make sure they are same files'''

def getMD5(path):
    d5 = hashlib.md5()      #生成一个hash的对象
    with open(path,'rb') as f:
        while True:
            content = f.read(40960)   # 每次读取40960大小，防止打开大文件导致内存溢出
            if not content:
                break
            d5.update(content)   # 每次读取一部分，多次调用，和一次性调用效果一样
    # print('MD5 : %s' % d5.hexdigest())
    return d5.hexdigest()        # 16进制的hash值

def getSha512(path):
    sh = hashlib.sha512()
    with open(path,'rb') as f:
        while True:
            content = f.read(40960)
            if not content:
                break
            sh.update(content)
    # print(sh.hexdigest())
    return sh.hexdigest()

def walk(path):
    x = input('Want to delete duplicate file? y/n\n')
    if x.lower() == 'y':
        delete = True
    else:
        delete = False
    dict = {}
    n = 1
    for folder,subfolder,filenames in os.walk(path):
        for filename in filenames:
            print('\rHas scanned %s files' %n,end='')
            root = os.path.join(folder,filename)
            md5 = getMD5(root)
            if md5 in dict:
                sha1 = getSha512(root)
                sha2 = getSha512(dict[md5])
                if sha1 == sha2:
                    # delete to recycle_bin
                    if delete == True:
                        send2trash.send2trash(dict[md5])
                    print('\n%s\n%s\n' %(root,dict[md5]))
            else:
                pass
            dict[md5] = root
            n += 1
    print('\nDone.')

if __name__ == '__main__':
    path = input('Input path:\n')
    walk(path)

# fa4ee7d173f2d97ee79022d1a7355bcf

import hmac
message = b'Hello,'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
h.update(b' world!')
# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())