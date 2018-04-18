import socket
import hashlib
import time
import math

s = socket.socket()
s.bind(("localhost", 8888))
s.listen(5)
c, addr = s.accept()
print "Connected to client ", addr

choice = int(c.recv(1))

hashObject = hashlib.sha1()

if( choice == 1 ):
	print "Client has requested for Text File...\n"
	with open('text.txt', 'rb') as text:
		message = text.read(1024)
		while(message):
			c.send(message)
			hashObject.update(message)
			message = text.read(1024)
elif( choice == 2 ):
	print "Client has requested for Image File...\n"
	with open('image.jpg', 'rb') as image:
		message = image.read(1024)
		while(message):
			c.send(message)
			hashObject.update(message)
			message = image.read(1024)
elif( choice == 3 ):
	print "Client has requested for Audio File...\n"
	with open('audio.mp3', 'rb') as audio:
		message = audio.read(1024)
		while(message):
			c.send(message)
			hashObject.update(message)
			message = audio.read(1024)
elif( choice == 4 ):
	print "Client has requested for Video File...\n"
	with open('video.mp4', 'rb') as video:
		message = video.read(1024)
		while(message):
			c.send(message)
			hashObject.update(message)
			message = video.read(1024)
		
hexDig = hashObject.hexdigest()
hashS = str(hexDig)
time.sleep(1)
c.send("BRK" + "\t" + hashS)

c.close()
