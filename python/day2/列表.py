names = ["wangzhongtao",'xiaoyi','liangmeng']
names.append('fengliang')
print(names)
names.insert(1,'chenchen')
print(names)
names.remove('wangzhongtao')
print(names)
del names[0]
print(names)
pop = names.pop()
print(names.index('liangmeng'))
# names.reverse()
names.sort()
print(names)
names2 = [1,2,3,4,5]
names.extend(names2)
del names2
print(names)

# 步长打印
print(names[0:-1:2]) # print(names[::2}

# 列表生成器
list2 = [x*3 for x in range(10)]
print(list2)