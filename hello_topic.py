from confluent_kafka import Producer
from config import Config
import json
    
def callback(err,event):
    if err:
        print(f"Produce event to topic {event.topic()} failed for event: {event.key()}")
    else:
        val = event.value().decode('utf-8')
        print(f'{val} sent to partition {event.partition()}')
        
def say_hello(producer,key):
    value = f'Hello {key}!'
    producer.produce('newTopic',value,key,on_delivery=callback)
    
if __name__ == '__main__':
    # with open("C:\\Users\\ppradeep\\.confluent\\python.properties", "r") as jsonfile:
    #     conf = json.load(jsonfile)
    #     print("Read successful")
    # print(conf)
    # cfg = Config("C:\\Users\\ppradeep\\.confluent\\kafka.cfg")
    # print(cfg.to)
    producer = Producer({
     'bootstrap.servers': '<bootstrap_server>',     
     'security.protocol': 'SASL_SSL',
     'sasl.mechanisms': 'PLAIN',
     'sasl.username': '<api_key>', 
     'sasl.password': '<api_val>'})
    keys = ['amy','prashanth','faraz']
    [say_hello(producer, key) for key in keys]
    producer.flush()