name = input('name:')
age = input('age:')

info = '''
name:{_name}
age:{_age}
'''.format(_name=name,_age=age)
print(info)
print('name is : %s,age is : %s'%(name,age))