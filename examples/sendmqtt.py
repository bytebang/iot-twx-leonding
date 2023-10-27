import paho.mqtt.client as mqtt
from sense_hat import SenseHat

# Datenquelle
sense = SenseHat()

# MQTT-Broker-Verbindungsinformationen
broker_address = "your.mqtt.broker.here"
broker_port = 1883
mqtt_topic = "iot-pi-hg/humidity"
username = "your_username"
password = "your_password"

# MQTT-Client initialisieren
client = mqtt.Client()
client.username_pw_set(username, password)

# Verbindung zum MQTT-Broker herstellen
client.connect(broker_address, broker_port)

# Nachricht veröffentlichen
message = sense.get_humidity()
client.publish(mqtt_topic, message)

# MQTT-Client sauber beenden
client.disconnect()
