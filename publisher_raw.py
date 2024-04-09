#Esse aqui é o publisher de teste, sem OOP e de forma simples.

import pika

connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

channel = pika.BlockingConnection(connection_parameters).channel()
#Isso aqui cria o canal de comunicação.

#Publisher só se relaciona com Exchange, então nao o conectamos a uma queue

channel.basic_publish(
    exchange="DataExchange",
    routing_key="", #Vazio pois não o utilizaremos
    body="Oi, eu sou uma mensagem",
    properties=pika.BasicProperties(
        delivery_mode=2
        #Delivery mode = 2 garante persistencia dos dados.
    )
)
#Isso tudo aqui é a nossa publicação