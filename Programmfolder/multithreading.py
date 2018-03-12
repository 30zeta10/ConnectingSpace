import threading
import thread
import random
import time

def actually_time():
		print (time.ctime()+"\n")

def random_number():
		print(str(random.randint(0,5))+"\n" )

while True:
	try:
		#Bei Parametern fuer die Funktion, kannst du args benutzen
		#threading.Thread(target=f, args=(a,b,c)).start()
		threading.Thread(target=actually_time).start()
		threading.Thread(target=random_number).start()
	except:
		print "thread is unable to start"
