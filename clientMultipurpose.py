import socket
import hashlib

s = socket.socket()
s.connect(("localhost", 8888))

choice = int(raw_input("1. Text\n2. Image\n3. Audio\n4. Video\nEnter Choice: "))
s.send(str(choice))

hashObject = hashlib.sha1()
receivedData=""

if( choice == 1 ):
	fw = open('received.txt','wb')
	print "Received text file is in 'received.txt' file"
	receivedData = s.recv(1024)
	while(receivedData):
		if (receivedData.split("\t")[0] == "BRK"):
			break
		fw.write(receivedData)
		hashObject.update(receivedData)
		receivedData = s.recv(1024)
elif( choice == 2 ):
	fw = open('received.jpg','wb')
	print "Received image file is in 'received.jpg'"
	receivedData = s.recv(1024)
	while(receivedData):
		if (receivedData.split("\t")[0] == "BRK"):
			break
		fw.write(receivedData)
		hashObject.update(receivedData)
		receivedData = s.recv(1024)
elif( choice == 3 ):
	fw = open('received.mp3','wb')
	print "Received audio file is in 'received.mp3'"
	receivedData = s.recv(1024)
	while(receivedData):
		if (receivedData.split("\t")[0] == "BRK"):
			break
		fw.write(receivedData)
		hashObject.update(receivedData)
		receivedData = s.recv(1024)
elif( choice == 4 ):
	fw = open('received.mp4','wb')
	print "Received video file is in 'received.mp4'"
	receivedData = s.recv(1024)
	while(receivedData):
		if (receivedData.split("\t")[0] == "BRK"):
			break
		fw.write(receivedData)
		hashObject.update(receivedData)
		receivedData = s.recv(1024)
	
receivedHash = receivedData.split("\t")[1]
print "Received Hash: ", receivedHash

hexDig = hashObject.hexdigest()
hashS = str(hexDig)
print "Hash of Received file: ", hashS

if(receivedHash == hashS):
	print "No Tampering in received file\n"
else:
	print "Tampering in received file\n"


