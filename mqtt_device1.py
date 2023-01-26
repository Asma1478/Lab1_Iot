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

def on_connect(client, userdata, flags, rc):
    global FLAG_CONNECTED
    
 
    if rc == 0:
        FLAG_CONNECTED = 1
        print(f'Connecting to broker: {BROKER}')
        
        print(f'Connecting to: {BROKER}, port: {PORT}')
        print(f"Publishing to topic: {TOPIC_UP}")
        print('Sending messages...\n')
    else:
        print("Failed to connect, return code {rc}".format(rc=rc), )
    
 
def connect_mqtt():
    client = mqtt_client.Client(CLIENT_ID)
    client.on_connect = on_connect
    client.connect(BROKER, PORT, keepalive=60)
    return client
 
 
client = connect_mqtt() 
client.loop_start()
time.sleep(1)
 
msg_count = 1
now = datetime.now()
dt = now.strftime("%Y-%m-%d %H:%M:%S")



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
  
    
    
    result = client.publish(TOPIC_UP, js_data)    
    
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print("Sensor data: {Tempeture}° C at time : {Time}  Message id: {message id/counter} ".format(**data))
        
        print(f'Publishing to topic: {TOPIC_UP}, JSON payload: {js_data}\n')
        
        
        
    else:
        print("Failed to send message to topic {topic}".format(topic=TOPIC_UP))
    msg_count += 1
    time.sleep(1)

  
 




 
  
 
  
 

