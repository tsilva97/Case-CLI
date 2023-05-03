from kafka import KafkaConsumer
from kafka import TopicPartition
from json import loads


def createConsumer(topic, partition):
    consumer = KafkaConsumer(bootstrap_servers=['localhost:9094'], auto_offset_reset='earliest', enable_auto_commit=False)
    consumer.assign([TopicPartition(topic,partition)])
    return consumer

def getMessages(consumer):
    for message in consumer:
        key = message.key.decode('utf-8')
        if message.value is not None:
            value = loads(message.value.decode('utf-8'))
        else:
            value = "Redacted"
        print ("%s:%d key= %s value= %s" % (message.topic, message.partition, key, value), flush=True)