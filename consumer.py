#Esse é o consumer pronto com a classe criada de forma eficiente


import pika

class RabbitmqConsumer:
    def __init__(self, callback) -> None:
        self._host = "localhost"
        self._port = 5672
        self._username = "guest"
        self._password = "guest"
        self._queue = "DataQueue"
        self._callback = callback
        self._channel = self.__create_channel()

    def __create_channel(self):  
        connection_parameters = pika.ConnectionParameters(
            host=self._host,
            port=self._port,
            credentials=pika.PlainCredentials(
                username=self._username,
                password=self._password
            )
        )

        channel = pika.BlockingConnection(connection_parameters).channel()

        channel.queue_declare(
            queue=self._queue,
            durable=True
        )

        channel.basic_consume(
            queue=self._queue,
            auto_ack=True,
            on_message_callback=self._callback
        )
        
        return channel

    def start(self):  
        print(f"Listen RabbitMQ on Port 5672")
        self._channel.start_consuming()

def minha_callback(ch, method, properties, body):
    print(body)

rabitmq_consumer = RabbitmqConsumer(minha_callback)
rabitmq_consumer.start()  
