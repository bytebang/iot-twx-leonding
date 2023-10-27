import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # After being connected, publish a message:
    client.publish("htl/iot-pi/hg", "Hello MQTT over WebSockets!")

def on_publish(client, userdata, mid):
    print("Message Published!")

# Set up the client
# Use transport="websockets" for WebSocket connection
client = mqtt.Client(transport="websockets")  

client.on_connect = on_connect
client.on_publish = on_publish

# Connect to a public MQTT broker that supports WebSockets (test.mosquitto.org in this example)
#client.connect("test.mosquitto.org", 8080, 60)  # Port 8080 for WS
client.connect("broker.mqttdashboard.com", 8000, 60)  # Port 8080 for WS

# MQTT-Client sauber beenden
client.disconnect()
