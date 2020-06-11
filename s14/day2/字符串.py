name = 'ALLix9'
print(name.casefold())  # 大写变成小写
name.lower()
print('10'.isnumeric())  #判断是否是数字，正整数
print(name.isalnum())    #判断是否数字加字母
print('Alsdf'.isalpha()) #判断是否是字母
print('.'.join(['a','b'])) #列表组成字符串
# 字符串替换或者叫翻译
str1 = 'abcde'
str2 = '12345'
trans = str.maketrans(str1,str2)  # 用str2里面的字符替换到str1里面对应的字符，两者长度必须一致一一对应
print('adbecLKI'.translate(trans))
print(name.swapcase())  # 大小写切换
print(name.ljust(40,'-'))
print(name.rjust(40,'-'))
print(name.isidentifier()) # 判断字符串是否符合变量命名规则


