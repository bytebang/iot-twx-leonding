#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid     = "htlleonding-seminar";
const char* password = "Fortbildung@HTL23";

const char* broker_host = "vm90.htl-leonding.ac.at";
const char* username = "student";
const char* passwd = "passme";

WiFiServer server(80);
WiFiClient wifiClient;


void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}

PubSubClient client(wifiClient);

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect(broker_host, username, passwd)) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("esp32", "hello from ESP32");
      Serial.print("Published");
      // ... and resubscribe
      client.subscribe("htlkaindorf/esp32/onReset");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup()
{
  //Wire.begin();
  Serial.begin(115200);

  delay(10);

  // We start by connecting to a WiFi network
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  server.begin();

  client.setServer(broker_host, 1883);
  client.setCallback(callback);

  Serial.println("Thingwork MQTT Demo connected");

}

int value = 0;

void loop() {
  float result[3] = {0};
  char message[20] = {0};

  for(int i = 0; i < 3; i++){
    result[i] = random(50) * 1.0f;
  }

  if (!client.connected()) {
    reconnect();
  }

  client.loop();
  sprintf(message, "%04.2f;%02.2f;%02.2f", result[0], result[1], result[2]);
  Serial.println(message);
  client.publish("htlkaindorf/esp32/random", message);

  delay(2000);
}

