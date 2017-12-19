import socket

#Informationen des Servers an dem gesendet wird
#Aktuell sendet er diesen an den localhost, da wir es auf einem Produkt testen
cest = '127.0.0.1'
port = 5555
addr = (dest,port)

#File-Informationen
buffersize = 8192
voice_file = "recording_voice.mp3"

#Lesen die Daten in den buffer
buff = open(voice_file).read()

#Verbindung und Sendung
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)
client.send(buf)

client.close()
