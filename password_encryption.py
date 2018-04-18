from Tkinter import *
from pyDes import *
i=1

def des1():
	txt=raw_input("Enter the text for encryption using DES => ")
	txt = txt.encode('utf-8')
	key=raw_input("Enter the key of size 8  => ")
	key=key.encode('utf-8')
	k = des(key, CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
	ciphered =k.encrypt((txt))
	print "Encrypted Text =>  %r" % ciphered

def Ceasar():
	txt=raw_input("Enter the text for encryption using CEASAR CIPHER => ")
	enTxt=[]
	for i in range(0,len(txt)):
		if(((ord(txt[i]))>=97) and ((ord(txt[i])<=122))):
			if(ord(txt[i])==122):
				enTxt.append('a')
			else:
				enTxt.append(chr(ord(txt[i])+1))
		elif(((ord(txt[i]))>=65) and ((ord(txt[i])<=90))):
			if(ord(txt[i])==90):
				enTxt.append('A')
			else:
				enTxt.append(chr(ord(txt[i])+1))
		else:
			enTxt.append(0)	
	str1 = ''.join(enTxt)
	print "Encrypted Text =>  ",str1
	
def Hill():
	txt=raw_input("Enter the text for encryption using HILL CIPHER => ")
	key=raw_input("Enter the key of size 9  => ")
	matrix=[]
	plaintxt=[]
	if((len(key)%len(txt))==0):
		for i in range(0,len(key)/len(txt)):
			matrix.append([])
			plaintxt.append(ord(txt[i])%97)
			for j in range(0,len(txt)):
					matrix[i].append(ord(key[i*len(txt)+j])%97)
    
	else:
			None
	newCipherMatrix=[]
	for i in range(0,len(key)/len(txt)):
			sum=0
			for j in range(0,len(txt)):
				sum=matrix[i][j]*plaintxt[j]+sum
			sum=sum%26
			newCipherMatrix.append(sum)
	newText=[]
	for i in range(0,len(newCipherMatrix)):
		newText.append(chr(newCipherMatrix[i]+97))
	str1 = ''.join(newText)
	print "Encrypted Text =>  ",str1
while(True):
	n=raw_input("\n\nChoose your option => \n\t1. DES \n\t2. CEASAR CIPHER \n\t3. HILL CIPHER \n\n")
	if n == "1":
		des1()
	elif n== "2":
		Ceasar()
	elif n == "3":
		Hill()
	elif n<3:
		print "\n\nWrong Option selected !"

	
	
