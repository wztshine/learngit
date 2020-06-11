'''
时间的三种格式：
1）时间戳 2）格式化的时间字符串 3）元组（struct_time） 9个元素
3. time.struct_time(tm_year=1970, tm_mon=5, tm_mday=23, tm_hour=20, tm_min=7, tm_sec=14, tm_wday=5, tm_yday=143, tm_isdst=0)
'''



import time

timeStamp = time.time()
print(timeStamp) # 当前时间；时间戳格式

# 时间戳--->元组
print(time.gmtime(12341234))  # 时间元组；获取某个时间戳的UTC时间（不写参数则为当前时间）
print(time.localtime())       # 时间元组；获取某个时间戳的本地时间（不写参数则为当前时间）
print(time.localtime().tm_year)  # 获取元组中某个元素的值

# 时间元组--->时间戳
tupleTime = time.localtime()    # 当前时间的时间元组
print(time.mktime(tupleTime))   # 时间戳

# 时间元组--->格式化字符串
print(time.strftime('%Y-%m-%d %H:%M:%S, %a,%A,%b,%B,%c,%I,%j,%p,%U,%w,%W,%x,%X,%y',tupleTime))
print(time.strftime('%x %X',tupleTime))
''' 
%a    本地（locale）简化星期名称    
%A    本地完整星期名称   
%b    本地简化月份名称    
%B    本地完整月份名称    
%c    本地相应的日期和时间表示    
%d    一个月中的第几天（01 - 31）    
%H    一天中的第几个小时（24小时制，00 - 23）    
%I    第几个小时（12小时制，01 - 12）    
%j    一年中的第几天（001 - 366）    
%m    月份（01 - 12）    
%M    分钟数（00 - 59）    
%p    本地am或者pm的相应符    
%S    秒（01 - 61）    
%U    一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。    
%w    一个星期中的第几天（0 - 6，0是星期天）    
%W    和%U基本相同，不同的是%W以星期一为一个星期的开始。    
%x    本地相应日期    
%X    本地相应时间    
%y    去掉世纪的年份（00 - 99）    
%Y    完整的年份    
%Z    时区的名字（如果不存在为空字符）    
%%    ‘%’字符'''

# 格式化时间字符串--->时间元组
print(time.strptime('2019-12-01 21:29:30','%Y-%m-%d %H:%M:%S'))

# 固定格式的字符串: Wed Oct 23 21:43:19 2019
# 时间元组/时间戳--->固定格式字符串
print(time.asctime())
print(time.ctime(timeStamp))


# datetime
import datetime
print('datetime'.center(50,'-'))
current_time = datetime.datetime.now()
print(current_time)                 # 当前格式化时间
print(datetime.date.fromtimestamp(timeStamp))  # 时间戳转换成年月日
print(datetime.datetime.now()+datetime.timedelta(3))  # 三天后的时间，可以为负数，为几天前
print(datetime.datetime.now()+datetime.timedelta(hours=3)) # 几小时后
print(datetime.datetime.now()+datetime.timedelta(minutes=3))
print(datetime.datetime.now()+datetime.timedelta(weeks=3))

# 时间的替换
print(current_time.replace(year=2012,month=12,day=12,hour=12,minute=12,second=12,microsecond=12))








