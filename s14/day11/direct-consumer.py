import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', # 声明一个exchange的名字和类型
                         exchange_type='direct')

result = channel.queue_declare('',exclusive=True)# 随机生成一个唯一的queue
queue_name = result.method.queue

severities = sys.argv[1:]  # 从命令行获取参数
if not severities:
    # sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    # sys.exit(1)
    severities = ['info']


for severity in severities:
    channel.queue_bind(exchange='direct_logs', # 绑定到direct_logs上
                       queue=queue_name,
                       routing_key=severity) # 指向相应的生产者上

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(queue_name,
                      callback,
                      auto_ack=True)
channel.start_consuming()