import re

'''
1. 匹配模式
^           匹配行首
$           匹配行尾
[]          匹配包含在中括号中的任意字符eg. [abc]
[^]         匹配包含在中括号中的字符之外的字符eg. [^0-9]
[-]         匹配指定范围的任意单个字符eg.[a-z0-9A-Z]
{n,}        配置之前项至少n次
'.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
'^'     匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
'$'     匹配字符结尾，或e.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE).group()也可以
'*'     匹配*号前的字符0次或多次，re.findall("ab*","cabb3abcbbac")  结果为['abb', 'ab', 'a']
'+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
'?'     匹配前一个字符1次或0次；非贪心模式
'{m}'   匹配前一个字符m次
'{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
'|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
'(...)' 分组匹配，re.search("(abc){2}a(123|456)c", "abcabca456c").group() 结果 abcabca456c
'\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
'\Z'    匹配字符结尾，同$
'\d'    匹配数字0-9
'\D'    匹配除0到9的数字以外的任何字符
'\w'    匹配任何字母、数字或下划线字符（可以认为是匹配“单词”字符）
'\W'    匹配除字母、数字和下划线以外的任何字符
's'     匹配空白字符：空格、制表符或换行符, re.search("\s+","ab\tc1\n3").group() 结果 '\t'
\S      除空格、制表符和换行符以外的任何字符
'(?P<name>...)' 分组匹配 re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city") 结果{'province': '3714', 'city': '81', 'birthday': '1993'}

2. 常用方法
re.match 从头开始匹配，返回一个SRE_Match类型的对象，否则返回None
re.search 从字符串任意位置中匹配，返回一个SRE_Match类型的对象，否则返回None
re.findall 把所有匹配到的字符放到以列表中的元素返回
re.splitall 以匹配到的字符当做列表分隔符
re.sub      匹配字符并替换

3. 参数 flags = re.IGNORECASE
如果想同时使用两个以上的此参数，可以使用|，如 re.I | re.M | re.S
re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
re.M(MULTILINE): 多行模式，忽略换行\n
re.S(DOTALL): 点任意匹配模式，改变'.'的行为，可以搜索所有,包括换行符

'''

# findall方法，该方法在字符串中查找模式匹配，将所有的匹配字符串以列表的形式返回，否则返回一个空的列表
re_str = "hello this is python 2.7.13 and python 3.4.5"
pattern = "python [0-9]\.[0-9]\.[0-9]"
res = re.findall(pattern=pattern, string=re_str) # res = re.findall(pattern, re_str)
print(res)

# 我们一般采用编译的方式使用python的正则模块，如果在大量的数据量中，编译的方式使用正则性能会提高很多
re_str = "hello this is python 2.7.13 and Python 3.4.5"
re_obj = re.compile(pattern = "python [0-9]\.[0-9]\.[0-9]",flags=re.IGNORECASE) # Regex对象
res = re_obj.findall(re_str)
print(res)

# match()
# match方法，从头开始匹配，match函数用以匹配字符串的开始部分，如果模式匹配成功，返回一个SRE_Match类型的对象，否则返回None
s_true = "123what is a boy"
s_false = "what is a boy"
re_obj = re.compile("what")
print(re_obj.match(string=s_true))
# <_sre.SRE_Match object; span=(0, 4), match='what'
print(re_obj.match(string=s_false))
# None
print(re_obj.match(string=s_true).group())  # Match对象获取值

#  search() ,同match
# search方法，模式匹配成功后，也会返回一个SRE_Match对象，search方法和match的方法区别在于match只能从头开始匹配，而search可以从
# 字符串的任意位置开始匹配，他们的共同点是，如果匹配成功，返回一个SRE_Match对象，如果匹配失败，返回一个None，这里还要注意，
# search仅仅查找第一次匹配，也就是说一个字符串中包含多个模式的匹配，也只会返回第一个匹配的结果，如果要返回所有的结果，最简单
# 的方法就是findall方法，也可以使用finditer方法

# sub() 替换方法
re_str = "what is a different between python 2.7.14 and python 3.5.4"
re_obj = re.compile("\d{1,}\.\d{1,}\.\d{1,}")
print(re_obj.sub("a.b.c", re_str, count=1)) # 替换一次
# what is a different between python a.b.c and python 3.5.4
print(re_obj.sub("a.b.c", re_str, count=2)) # 替换两次
# what is a different between python a.b.c and python a.b.c
print(re_obj.sub("a.b.c", re_str))  # 全部替换
# what is a different between python a.b.c and python a.b.c

# split() 分割字符串
re_str = "what is a different between python 2.7.14 and python 3.5.4 USA:NewYork!Zidan.FRA"
re_obj = re.compile("[. :!]") # 按照此列表的元素来分割
print(re_obj.split(re_str))
# ['what', 'is', 'a', 'different', 'between', 'python', '2', '7', '14', 'and', 'python', '3', '5', '4', 'USA', 'NewYork', 'Zidan', 'FRA']

# 4、非贪婪匹配，贪婪匹配总是匹配到最长的那个字符串，非贪婪匹配是匹配到最小的那个字符串，只需要在匹配字符串的时候加一个？即可
# 下面的例子，注意两个.
s = "Beautiful is better than ugly.Explicit is better than impliciy."
re_obj = re.compile("Beautiful.*y\.")
print(re_obj.findall(s))
# ['Beautiful is better than ugly.Explicit is better than implicit.']
re_obj = re.compile("Beautiful.*?y\.")
print(re_obj.findall(s))
# ['Beautiful is better than ugly.']


