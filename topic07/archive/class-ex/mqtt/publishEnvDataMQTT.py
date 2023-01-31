#!/usr/bin/python3

#**************************************
#For this script to work you will need
#1. Create a channel in Thingspeak
#2. Add a device to thingspealk
#3. Download the device credentials as txt file
#4. Place the device credentials in the .env file
#5. update the topic variable with the Channel ID from Thingspeak
#****************************************

import paho.mqtt.client as mqtt
from urllib.parse import urlparse
import sys
import time
import json
from sense_hat import SenseHat
from dotenv import dotenv_values

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("Connection Result: " + str(rc))

def on_publish(client, obj, mid):
    print("Message ID: " + str(mid))

sense = SenseHat()
sense.clear()
#load configuration values from .env file
config = dotenv_values(".env")
interval = int(config["transmissionInterval"])

mqttc = mqtt.Client(client_id=config["clientId"])

# Assign event callbacks
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

# connect to Broker
mqttc.username_pw_set(config["username"], config["password"])
mqttc.connect("mqtt3.thingspeak.com", 1883)
mqttc.loop_start()
topic = "channels/GET_CHANNEL_ID_FROM_THINGSPEAK/publish"

# Publish a message to temp every 15 seconds
while True:
        temp=round(sense.get_temperature(),2)
        payload="field1="+str(temp)
        mqttc.publish(topic, payload)
        time.sleep(interval)