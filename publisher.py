from typing import Dict
import pika
import json

class RabbitmqPublisher:
    def __init__(self) -> None:
        self._host = "localhost"
        self._port = 5672
        self._username = "guest"
        self._password = "guest"
        self._exchange = "DataExchange"
        self._routing_key = ""
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
        return channel
    
    def send_message(self, body: Dict):
        self._channel.basic_publish(
            exchange=self._exchange,
            routing_key=self._routing_key,
            body=json.dumps(body),  # Enviar um JSON pelo body
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )

#Cria o objeto
rabbitmq_publisher = RabbitmqPublisher()

# Aqui a gente pode enviar um json
rabbitmq_publisher.send_message({"mensagem": "Aqui fica a mensagem"})
