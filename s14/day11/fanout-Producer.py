import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',     # exchange随意设置一个叫 logs
                         exchange_type='fanout') # 类型用fanout,可以对所有绑定此exchange的channel进行广播

message = "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',  # 不设定routing_key,就是对所有channel进行推送消息
                      body=message)
print(" [x] Sent %r" % message)
connection.close()