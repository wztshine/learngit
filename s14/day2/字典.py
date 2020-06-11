'''特性：key唯一；无序'''
info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}

# 增删查改
info["stu1104"] = "苍井空"  #增
info['stu1101'] = "武藤兰"  #改
info.pop('stu1104')         #删
# del info['stu1104']         # 删
print('stu1101' in info)   # true
print(info.get('stu1106'))  # 查询
print(info['stu1101'])    # 如果没有stu1101，会报错，上面的get方法不会

info.setdefault("stu1106","Alex") # 如果没有key，就设置值Alex，否则不变


# update
b = {1:2,3:4,'stu1102':'泷泽萝拉'}
info.update(b)    # 合并更新两个字典，如果有相同的key，则更新此key，没有则添加key-value
print(info)



print(info.items())
# print(info.values())
# print(info.keys())


# 遍历
for key in info:          #高效
    print(key,info[key])

for k,v in info.items(): # 先把字典转成list，数据大时不要用
    print(k,v)


# 对字典排序
a = {1:23,99:2,28:72,3:83,72:222}
print(sorted(a))     # 对字典按照key排序，打印key的list
print(sorted(a.items()))   # 对字典按照key排序，打印键值对元组，list
print(sorted(a.items(),key=lambda x:x[1],reverse=True))   # 对字典按照value排序，可以逆序，打印键值对元组