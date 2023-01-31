#!/usr/bin/python3

#**************************************
#For this script to work you will need
#1. Create a channel in Thingspeak
#2. update the .env file with the channel write key
#****************************************

from urllib.request import urlopen
import  json
import  time
from sense_hat import SenseHat
from dotenv import dotenv_values

#load configuration values from .env file
config = dotenv_values(".env")
baseURL="https://api.thingspeak.com/update?api_key=" + config["apiWriteKey"]

interval = int(config["transmissionInterval"])
sense = SenseHat()

def writeData(temp):
    # Sending the data to thingspeak in the query string
    print(baseURL + "&field1=" +str(temp))
    conn = urlopen(baseURL + "&field1=" +str(temp))
    print(conn.read())
    # Closing the connection
    conn.close()

while True:
    temp=round(sense.get_temperature(),2)
    writeData(temp)
    time.sleep(interval)