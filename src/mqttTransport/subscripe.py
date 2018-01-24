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

mqttc.username_pw_set(user, pw)
mqttc.connect(host, port)

mqttc.subscribe(topic, 0)

mqttc.loop_stop()
rc = 0

while rc == 0:
    rc = mqttc.loop()
print("rc: " + str(rc))
