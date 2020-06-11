import random

print(random.random())       # 0< x <1  的浮点数
print(random.uniform(1,5))   # 1<x <5 的浮点数
print(random.randint(1,2))   #  1<= x < =2 的整数
print('jiii',random.randrange(1,10,2)) # 1<= x < 10 并且是奇数
print(random.choice('sdkf')) # 从列表中随机选择，参数可以为列表、元组等
print(random.sample('sdkf',2)) # 从列表、元组、字符串中随机选取多个
x = [1,2,3,4,5]
random.shuffle(x)  # 打乱list顺序
print(x)


char = ''
for i in range(0,5):
    current = random.randrange(0,5)
    if current == i:
        char += str(i)
    else:
        char+=chr(random.randint(65,90))
print(char)
