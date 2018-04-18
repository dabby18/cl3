import json
columns=[0,1,2,3,4,5,6,7,8]
boardSize=8
global flag
def nQueen(row):
	global flag
	for i in range(1,boardSize+1):
		if (safePlace(row,i)==True):
			columns[row]=i;
			if(row==boardSize):
				if(flag==0):
					print ("\nSolutions that satisfy the given condition are:")
				print (columns[1:boardSize+1])
				flag=1
			else:
				nQueen(row+1)

def safePlace(row,i):
	for j in range (1,row):
		if((columns[j]==i) or (abs(columns[j]-i)==abs(j-row))):
			return False
	return True
	
data=[]
flag=0
with open('input.json') as f:
	data=json.load(f)
    
if(data["start"]<1 or data["start"]>8):
        print("\nInvalid JSON input.\n")
        exit()
print ("\nFirst queen is placed in column: ",data["start"])
columns[1]=data["start"]      
nQueen(2)
if(flag==0):
	print("\nNo solution satisfying the given conditon is found.\n")
