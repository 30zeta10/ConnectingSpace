import paho.mqtt.client as mqtt
import wave
import audioop

def publishMqtt(message):

    usF = open("/home/zeta/Dokumente/secrets/user", "r")
    pwF = open("/home/zeta/Dokumente/secrets/pw", "r")

    user = usF.read().rstrip()
    pw = pwF.read().rstrip()
    topic = '/voice/'
    host = "m23.cloudmqtt.com"
    port = 16533

    def on_message(client, obj, msg):
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


    mqttc = mqtt.Client()

    mqttc.on_message = on_message

    mqttc.username_pw_set(user, pw)
    mqttc.connect(host, port)

    mqttc.publish(topic, message)

