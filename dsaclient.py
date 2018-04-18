import socket
import hashlib
import random
st = socket.socket()
port = int(raw_input("Enter the port number: "))
st.connect(("localhost",port))
q = st.recv(10)
q = int(q)
print "Value of q :",q
p = st.recv(10)
p = int(p)
print "Value of p :",p
g = st.recv(10)
g = int(g)
print "Value of g :",g
y = st.recv(10)
y = int(y)
print "Value of y :",y
print "Public key of server: p[",p,"] ,q[",q,"] ,g[",g,"] ,y[",y,"]"
msg = st.recv(1024)
print "Message from server :",msg
s = st.recv(10)
s = int(s)
print "The value of s :",s
r = st.recv(10)
r = int(r)
print "The value of r :",r
print "Digital signature by server: s[",s,"] ,r[",r,"]"
H = ord(hashlib.md5(msg).digest()[0])
w = random.randrange(1,100)
while((s*w)%q!=1):
	w = random.randrange(1,100)
u1 = H*w%q
u2 = r*w%q
v = (((g**u1)*(y**u2))%p)%q
print "The value of v :",v
if(v==r):
	print "Valid signature because v and r are equal"
else:
	print "Invalid signature"
