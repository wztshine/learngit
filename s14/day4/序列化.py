import json

s = {1:'a',2:'b',3:'c'}
# 1. dumps: obj-->string;从数据转成json字符串
ds = json.dumps(s)
print(ds,type(ds))

# 2. dump: obj-->file；从数据写入文件
with open('j','w') as f:
    d = json.dump(s,f)

# 3. loads: string-->obj；从json字符串转成数据
lds = json.loads(ds)
print(lds,type(lds))

# 4. load: file-->obj；从文件读取转成数据
with open('j','r') as f:
    ld = json.load(f)
    print(ld,type(ld))



import pickle
data = ['aa', 'bb', 'cc']

# 1. dumps(object) -> string；将数据转成只有python语言认识的字符串
p_str = pickle.dumps(data)
print(p_str)
# b'\x80\x03]q\x00(X\x02\x00\x00\x00aaq\x01X\x02\x00\x00\x00bbq\x02X\x02\x00\x00\x00ccq\x03e.

# 2. dump(object, file); 将数据转成pickle的字符串，并写入文件
with open('ak.pk', 'wb') as f:  # file必须以二进制可写模式打开，即“wb”
    pickle.dump(data, f)        # 文件里面存的是pickle的字符串，不是明文数据

# 3. load(file) -> object ；从文件读取pickle的字符串并转换成原来的数据格式
with open('ak.pk', 'rb') as f:  # 要以二进制读取打开
    data = pickle.load(f)
    print(data)          # data是明文数据
# ['aa', 'bb', 'cc']

# 4. loads(string) -> object；将pickle字符串转成python数据
mes = pickle.loads(p_str)
print(mes)
# ['aa', 'bb', 'cc']