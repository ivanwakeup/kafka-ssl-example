from psdvs.producer import Producer
from psdvs.avro_serializer import DVSAvroSerializer
from psdvs.string_serializer import StringSerializer

dvs_kafka_config = {
    "bootstrap.servers": "localhost:9093",
    "client.id": "DVS_PRODUCER",
    "default.topic.config": {"request.required.acks": 1},
    "max.in.flight.requests.per.connection": 1,
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

topic = "test.topic"
records = [("testkey", {"id": 1, "serial": "some-serial3"})]

producer = Producer(dvs_kafka_config)
key_seriazer = StringSerializer()
value_serializer = DVSAvroSerializer(schema_registry_config=dvs_schema_registry_config,
                                     topic=topic)


def delivery_callback(err, msg):
    if err:
        print(err)
    print(value_serializer.deserialize(msg.value()))


try:
    for key, value in records:
        keydata = key_seriazer.serialize(key)
        valuedata = value_serializer.serialize(value)
        producer.produce(topic=topic, value=valuedata, key=keydata, on_delivery=delivery_callback)
        producer.poll(0)
finally:
    producer.flush()
