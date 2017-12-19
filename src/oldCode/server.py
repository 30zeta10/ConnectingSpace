import socket

#Serverinformationen
dest = ''
port = 5555
addresse = (dest,port)
buffer_size = 8192

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bindet an den Port und hört ob ein Client sich meldet
server.bind(addresse)
serv.listen(5)

while True:

  #Erstellt die Verbindung
  connected, addr = serv.accept()

  my_file = open('recording_voice.mp3', 'w')

  #Empfangen die Tagen und schreiben sie in my_file bis wir keine Daten in data mehr haben
  while True:

    data = connected.recv(buffer_size)
    
    if(not data): 
      break
   
    my_file.write(data)
   
  my_file.close()
  conncted.close()

