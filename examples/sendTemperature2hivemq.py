import paho.mqtt.client as paho

from paho import mqtt
from sense_hat import SenseHat

client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
sense = SenseHat()
 
# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set("iottest", "IotTest123")

# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("dc5a170db2354a828896bc071195f7dd.s2.eu.hivemq.cloud", 8883)

# a single publish, this can also be done in loops, etc.
client.publish("iot-pi-hg/temperature", payload=sense.get_temperature(), qos=1)

# ciao
client.disconnect()
