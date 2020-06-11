import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

# 声明queue
channel.queue_declare(queue='hello',durable=True) # durable=True,将队列持久化，哪怕 RabbitMQ服务重启，此队列依然存在

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!',
                      properties=pika.BasicProperties(delivery_mode=2) # 将队列中的消息也持久化
                      )
print(" [x] Sent 'Hello World!'")
connection.close()