#from sense_hat import SenseHat
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import random
from datetime import datetime
#sense = SenseHat()

Broker = "195.154.113.229"

sub_topic = "sensor/instructions"    # receive messages on this topic

pub_topic = "sensor/data"       # send messages to this topic


############### sensehat inputs ##################

def read_temp():
    #t = sense.get_temperature()
    t =  randomDelay = random.randint(0,40)
    t = round(t)
    return t

def read_humidity():
    #h = sense.get_humidity()
    h =  randomDelay = random.randint(0,100)
    h = round(h)
    return h

def read_pressure():
    p =  randomDelay = random.randint(15,100)
    #p = sense.get_pressure()
    p = round(p)
    return p

def display_sensehat(message):
    sense.show_message(message)
    time.sleep(10)

############### MQTT section ##################

# when connecting to mqtt do this;

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(sub_topic)
    print("connected")

# when receiving a mqtt message do this;

def on_message(client, userdata, msg):
    message = str(msg.payload)
    print(msg.topic+" "+message)
    display_sensehat(message)

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))


client = mqtt.Client()
print("connected with result code ...")
client.on_connect = on_connect
client.on_message = on_message
client.connect(Broker, 1883, 60)
client.loop_start()

while True:
    sensor_data = {"time" : datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                   "temp" : read_temp(),
                   "humidity": read_humidity(),
                   "pressure" : read_pressure()}
    print(sensor_data ,"\n")
    client.publish("monto/solar/sensors", str(sensor_data))
    time.sleep(1*60)
