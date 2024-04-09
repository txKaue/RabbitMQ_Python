#Esse aqui é o consumer de teste, sem OOP e de forma simples.

import pika

def minha_callback(ch, method, properties, body):
    print(body)
    
#Isso aqui é uma ação condicional 

connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

channel = pika.BlockingConnection(connection_parameters).channel()
#Isso aqui é a conexão com RabbitMQ

channel.queue_declare(
    queue="DataQueue",
    durable=True
)

channel.basic_consume(
    queue="DataQueue",
    auto_ack=True,
    on_message_callback=minha_callback
)

print(f"Listen RabbitMQ on Port 5672")

channel.start_consuming()