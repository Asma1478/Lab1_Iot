import random
import time
from datetime import datetime
from paho.mqtt import client as mqtt_client
 
 
BROKER = 'broker.hivemq.com'
PORT = 1883
tobic = "hajo66/devices/node1/up"
# generate client ID with pub prefix randomly
CLIENT_ID = "python-mqtt-tcp-pub-{id}".format(id=random.randint(0, 1000))



def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            print("Subscribed to topic: hajo66/devices/node1/up")
            print("Waiting for messages...\n")
        else:
            print("Failed to connect, return code %d\n", rc)
 
    client = mqtt_client.Client(CLIENT_ID)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(BROKER, PORT)
    return client
 
 
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        now = datetime.now()
        dt = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Received  topic: {msg.topic} with payload: {msg.payload.decode()} at subscribers local time: {dt}\n")
       
 
    client.subscribe(tobic)
    client.on_message = on_message
 
 
def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
 
 
if __name__ == '__main__':
    run()