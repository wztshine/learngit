set1 = set([1,2,3,4])
set2 = set([3,4,5,6,7,8,9,10])

print('差集:'.ljust(20,' '),set1 - set2) # 差集，在1不在2
print('并集:'.ljust(20,' '),set1 | set2) # 1/2并集
print('对称差集:'.ljust(18,' '),set1 ^ set2) # 1/2不同的部分，对称差集
print('交集:'.ljust(20,' '),set1 & set2) # 1/2交集，相同部分
print(set1<=set2)       # set1是否是set2的子集
print(set2>=set1)      #set2是否是set1的父集

#添加一个和多个
set1.add(5)
set1.update([1,2,3,4,5,6,7])
print(set1)

# 集合删除
set1.remove(7)
