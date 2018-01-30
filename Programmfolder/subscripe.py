import paho.mqtt.client as mqtt

user = "pdqmkvuw"
pw = "G4CeJE2Qs-rh"
host = "m23.cloudmqtt.com"
port = 16533
checkmsg = None 

def on_message(client, obj, msg):
    
    f = open('msg.txt', 'wb')
    f.write(msg.payload)
    f.close

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.username_pw_set(user, pw)
mqttc.connect(host, port)

mqttc.subscribe('/voice/', 0)

rc = 0
while(rc == 0):
    rc = mqttc.loop()
