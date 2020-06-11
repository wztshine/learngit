import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

# 为什么又声明一遍这个队列（生产者已经声明过了），因为如果消费者先运行起来，此时又没有声明的话，会报错，
# 所以在这里重新声明一遍，防止出错罢了。
channel.queue_declare(queue='hello',durable=True) # durable=True,将队列持久化，哪怕 RabbitMQ服务重启，此队列依然存在


def callback(ch, method, properties, body):
    print('-->',ch,method,properties)
    # time.sleep(30)
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)   # 手动应答，只有消费者确认了，才会从队列删除

channel.basic_qos(prefetch_count=1)  # 如果一个消费者的队列中还有1个消息,就不继续推送给这个消费者

channel.basic_consume('hello',
                      callback,
                      # auto_ack=True  # 自动应答，消费者一收到消息，消息就自动从队列中删除，如果消费者没有处理完此消息，也会删除。
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()