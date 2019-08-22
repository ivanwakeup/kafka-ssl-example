from psdvs.consumer import Consumer
from psdvs.avro_serializer import DVSAvroSerializer

dvs_kafka_config = {
    "bootstrap.servers": "localhost:9092",
    "client.id": "MYCLIENT",
    "default.topic.config": {"request.required.acks": 1},
    "security.protocol": "SSL",
    "ssl.ca.location": "certs/ca-cert",
    "ssl.certificate.location": "stores/python/client_python_client.pem",
    "ssl.key.location": "stores/python/client_python_client.key",
    "ssl.key.password": "1111"
}

dvs_schema_registry_config = {
    "host": "localhost",
    "port": "8081",
}


def make_handler(topic):
    serializer = DVSAvroSerializer(topic=topic,
                                   schema_registry_config=dvs_schema_registry_config)

    def handle_message(key, msg, partition, offset):
        print(topic)
        print(repr(serializer.deserialize(msg)))
    return handle_message


consumer = Consumer(dvs_kafka_config, consumer_group="MYCONSUMERGROUP")
consumer.subscribe("test.topic",
                   callback=make_handler("test.topic"),
                   offset="latest")
consumer.run()
