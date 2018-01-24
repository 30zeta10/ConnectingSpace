import paho.mqtt.client as mqtt

topic = "/voice/"
user = "pdqmkvuw"
pw = "G4CeJE2Qs-rh"
host = "m23.cloudmqtt.com"
port = 16533

def on_message(client, obj, msg):
    print("Write")
    f = open('newpic.jpg', 'wb')
    f.write(msg.payload)
    f.close()

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.username_pw_set(user, pw)
mqttc.connect(host, port)

mqttc.subscribe(topic, 0)

rc = 0

while rc == 0:
    rc = mqttc.loop()
print("rc: " + str(rc))
