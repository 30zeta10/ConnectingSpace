import paho.mqtt.client as mqtt

topic = "/voice/"
user = "pdqmkvuw"
pw = "G4CeJE2Qs-rh"
host = "m23.cloudmqtt.com"
port = 16533


def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

mqttc = mqtt.Client()

mqttc.on_message = on_message

# Connect
mqttc.username_pw_set(user, pw)
mqttc.connect(host, port)

# Start subscribe, with QoS level 0
mqttc.subscribe(topic, 0)

# Publish a message
mqttc.publish(topic, "YEEEEEEES")

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
print("rc: " + str(rc))
