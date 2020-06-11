import logging
import logging.handlers
import datetime
import time


'''
CRITICAL	50
ERROR	    40
WARNING	    30
INFO	    20
DEBUG	    10
NOTSET	    0
'''

# # 设置相应的日志级别和格式，不写入文件的话会打印在屏幕. basicConfig :对root logger进行一次性配置,不设置日志等级是warning
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s',datefmt='%Y/%m/%d %H:%M:%S %p ')
# logging.warning('logging.warning')
# logging.info('logging.info')

# 创建一个logger
logger = logging.getLogger('log')
logger.setLevel(logging.DEBUG)   # 设置log等级

# handler1 ,负责生成 all_logs.log
# 添加handler, 决定日志落地到哪里，一个logger可以添加多个
# 按照时间回滚日志
apps_handler = logging.handlers.TimedRotatingFileHandler(filename='all_logs.log',
                                                         when='S',
                                                         interval=1,
                                                         backupCount=3,  # 保留3个
                                                         atTime=datetime.time(0, 0, 0, 0))
apps_handler.suffix="%Y-%m-%d_%H-%M-%S.log"
# 设置这个handler的处理格式， 实例化一个Formatter对象
apps_formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
apps_handler.setFormatter(apps_formatter)
logger.addHandler(apps_handler)

# handler2 生成error.log，处理ERROR的日志，并添加了一个过滤器,只会执行来自log.a的日志
apps_handler2 = logging.FileHandler(filename='error.log')
apps_formatter2 = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
apps_handler2.setFormatter(apps_formatter2)
# 设置handler的level
apps_handler2.setLevel(logging.ERROR)
handler2Filter = logging.Filter(name = 'log')  # 符合名字规范的都可以进来，如log.a;log.log2,如果命名为log.a，则下面的logger2的信息就无法进来了
apps_handler2.addFilter(handler2Filter)
logger.addHandler(apps_handler2)

logger2 = logging.getLogger('log.log2')    # 通过.传递层级，.后面的都是前面的children，默认会把消息传递给祖先，
logger2.setLevel(logging.DEBUG)
logger2.propagate = False  # 禁止传递，也就是不会把消息传递给上一层的logger，同时也拒绝了上级的设置，如logging.basicConfig
logger2.critical('CRITICAL info!!!')
logger2.error('2.error')
logger2.warning('2.warning')
logger2.info('2.info')
logger2.debug('logger2 2222debug info')

logger.debug('debug info')
logger.info('info info')
logger.warning('warning info')
logger.error('error info')
logger.critical('critical info')

while True:
    time.sleep(0.5)
    num = 1
    logger.info('This is %s %s',num,'times')
    num+=1


'''
解读：
1. 定义一个logger,设置日志级别
2. 定义一个handler，设置日志级别
3. 定义一个filter，设置日志级别
4. 把filter添加到handler里，把handler添加到logger里。（logger也可以添加过滤器)
5. 定义一个logger2，是logger的下一层级,设置日志级别，设置propagate是否传递。
6. logger2.debug(message),先检查logger2的日志级别，如果大于debug，则过滤掉不处理，否则处理。
   如果propagate为fasle，则不往上传递，否则还会传递给logger，logger继续处理
7. logger.warning(message),检查logger设置的日志等级，如果能对应上，分发到logger的handler，查看handler的日志
   以及handler的filter的规则，如果都通过，则按照handler定义的方式进行处理：如显示在控制台或者写入一个log文件等
'''


