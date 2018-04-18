import socket
import hashlib
import sys
import random
import time as t
st = socket.socket()
port = int(raw_input("Enter the port number: "))
st.bind(("localhost",port))
st.listen(5)
c,addr = st.accept()
start = 2
stop = 10
def isprime(ran):
	if(ran > 2):
		for i in range(2,ran):
			if(ran%i==0):
				return 0
		return 1
while(1):
	q = random.randrange(start,stop)
	if(q>2):
		result = isprime(q)
	if(result == 0):
		continue
	else:
		break
print "Value of q :",q
temp = str(q)
c.send(temp)
t.sleep(.2)
p=0
while((p-1)%q!=0):
	while(1):
		p = random.randrange(2,31)
		result = isprime(p)
		if(result == 0):
			continue
		else:
			break
print "Value of p :",p
temp = str(p)
c.send(temp)
t.sleep(.2)
g=random.randrange(1,p)
h=random.randrange(1,p-1)
while(g**q%p!=1):
	g = h**((p-1)/q)%p
x = random.randrange(0,q)
y = g**x%p
print "Value of g :",g
temp = str(g)
c.send(temp)
t.sleep(.2)
print "Value of x :",x
print "Value of y :",y
temp = str(y)
c.send(temp)
t.sleep(.2)
print "Public key of server: p[",p,"] ,q[",q,"] ,g[",g,"] ,y[",y,"]"
print "Private key of server: p[",p,"] ,q[",q,"] ,g[",g,"] ,x[",x,"]"
msg = raw_input("Enter the msg that you want to send : ")
c.send(msg)
t.sleep(.2)
H = ord(hashlib.md5(msg).digest()[0])
print "Hash vlue of message:",H
s=0
while(s==0):
	k = random.randrange(1,q)
	r=(g**k%p)%q
	#print "the value of r :",r
	while(r==0):
		k = random.randrange(0,q)
		r=(g**k%p)%q
		#print "The value of r:",r
	i = random.randrange(1,40)
	while(k*i%q!=1):
		i = random.randrange(1,40)
		#print "the value of i:",i
	s = i*(H+r*x)%q
	#print "the value of s :",s
print "The value of s:",s
temp = str(s)
c.send(temp)
t.sleep(.2)
print "The value of r:",r
temp = str(r)
c.send(temp)
t.sleep(.2)
print "Digital signature by server: s[",s,"] ,r[",r,"]"
