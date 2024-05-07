#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt #import library
import time

MQTT_BROKER = "localhost"
MQTT_TOPIC = "test_channel"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.connect(MQTT_BROKER)
msg="Hello World!!"
client.publish(MQTT_TOPIC,msg)
print("Published {} over MQTT".format(msg))
counter=0
while counter < 10:
    counter+=1
    teste = client.publish(MQTT_TOPIC,"counter : {}".format(counter))
    print(teste)
    time.sleep(0.1)
client.disconnect()

#sdshgh