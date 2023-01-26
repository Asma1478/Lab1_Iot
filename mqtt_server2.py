import json
import random
import time
from datetime import datetime
from paho.mqtt import client as mqtt_client
 
 
BROKER = 'broker.hivemq.com'
PORT = 1883
TOPIC_UP = "hajo66/devices/node1/up"
TOPIC_D = "hajo66/devices/node1/down"
# generate client ID with pub prefix randomly
CLIENT_ID = "python-mqtt-tcp-pub-{id}".format(id=random.randint(0, 1000))

FLAG_CONNECTED = 0
 
now = datetime.now()
dt = now.strftime("%Y-%m-%d %H:%M:%S")

def on_message(client, userdata, msg):
    print(f'Received topic: {msg.topic} with playload: {msg.payload} at subscribers local time: {dt}\n')
    time.sleep(1)

    

def on_connect(client, userdata, flags, rc):
    global FLAG_CONNECTED
    
    if rc == 0:
        FLAG_CONNECTED = 1
        print(f'Connecting to broker: {BROKER}')
        
        print(f'Connecting to: {BROKER}, port: {PORT}')
        print(f"Subscribed to topic: {TOPIC_UP}")
        print('Sending and Waiting for messages...\n')
    else:
        print("Failed to connect, return code {rc}".format(rc=rc), )
 
def connect_mqtt():
    client = mqtt_client.Client(CLIENT_ID)
    client.on_connect = on_connect
    client.connect(BROKER, PORT, keepalive=60)
    return client
 
 
client = connect_mqtt() 
client.subscribe(TOPIC_UP)
client.on_message = on_message
        
client.loop_start()
time.sleep(1)
 
msg_count = 1




while True:
    tem = random.randint(0, 70)    
    port_channel = random.randint(1,100)
    rssi = random.randint(-100,1)
    snr = random.randint(-50,100)
    now = datetime.now()
    dt = now.strftime("%Y-%m-%d %H:%M:%S")
  
    data = {'app_id': 'hajo66', 'dev_id': 'nodel', 'port/channel': port_channel, 
        'rssi': rssi, 'snr': snr, 'sf': 'SF7BW125', 'C_F': 'C','Tempeture': tem  ,'Time': dt, 'message id/counter': msg_count,
    }
    js_data = json.dumps(data, default=str)
  
    
    
    result = client.publish(TOPIC_D, js_data)    
    
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print("Sending ACK To Device: ACK_MSG_RECEIVED")
        
        print(f"Publishing to topic: {TOPIC_D}, JSON payload: ACK_MSG_RECEIVED")
        print("Message id: {message id/counter}\n".format(**data))
       
    else:
        print("Failed to send message to topic {topic}".format(topic=TOPIC_D))
    msg_count += 1
    time.sleep(5)
    


  
 




 
  
 
  
 

