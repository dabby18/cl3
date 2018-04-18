import java.io.*;
import java.net.*;
import java.util.Arrays;

public class MyServer {
	int a[], q[], q_1 = 0, m[], m_[];
	int n1, n2, nBits, flag = 0;
	ServerSocket ss;
	Socket s;
	DataInputStream dis;
	DataOutputStream dos;
	
	void establishConnection(){
		try{
			ss = new ServerSocket(8888);
			s = ss.accept();
			dis = new DataInputStream(s.getInputStream());
			dos = new DataOutputStream(s.getOutputStream());
		}	catch(Exception e){}	
		
	}
	
	void getData(){
		try{
			String str = (String)dis.readUTF();
			n1 = Integer.parseInt(str);
			int n1_ = -n1;
			char[] temp1 = Integer.toBinaryString(n1).toCharArray();
			char[] temp1_ = Integer.toBinaryString(n1_).toCharArray();
			
			if(n1<0)
				flag++;
			str = (String)dis.readUTF();
			n2 = Integer.parseInt(str);
			char[] temp2 = Integer.toBinaryString(n2).toCharArray();
			if(n2<0)
				flag++;
			str = (String)dis.readUTF();
			nBits = Integer.parseInt(str);
			
			//Store into variables
			//multiplicand (+M)
			m = new int[nBits];
			m_ = new int[nBits];
			a = new int[nBits];
			q = new int[nBits];
			
			for(int start = 1, end = nBits-1; start <= nBits; start++, end--){
				if(temp1.length-start >= 0)
					m[end] = temp1[temp1.length-start] - '0';
				else
					m[end] = 0;
			}
			//multiplicand (-M)
			for(int start = 1, end = nBits-1; start <= nBits; start++, end--){
				if(temp1_.length-start >= 0)
					m_[end] = temp1_[temp1_.length-start] - '0';
				else
					m_[end] = 0;
			}
			//multiplier(+Q)
			for(int start = 1, end = nBits-1; start <= nBits; start++, end--){
				if(temp2.length-start >= 0)
					q[end] = temp2[temp2.length-start] - '0';
				else
					q[end] = 0;
			}
			
			//accumulator(+A)
			Arrays.fill(a, 0);
			
			System.out.print("Number 1: ");
			for(int i = 0; i < nBits; i++)
				System.out.print(m[i]);
			
			System.out.print("\nNumber 2: ");
			for(int i = 0; i < nBits; i++)
				System.out.print(q[i]);
			System.out.println("\n---------------------------------------\nA\t\tQ\t\tQ-1");
			System.out.println("---------------------------------------");
		} catch(Exception e){}
	}
	
	void arithmeticShiftRight(){
		q_1 = q[nBits-1];
		int i;
		for(i = nBits-1; i > 0; i--)
			q[i] = q[i-1];
		q[0] = a[nBits-1];
		for(i = nBits-1; i > 0; i--)
			a[i] = a[i-1];
	}
	
	void addition(int[] y){
		int c = 0;
		for(int i = nBits-1; i >=0; i--){
			a[i] += y[i] + c;
			if(a[i]>1)
				c = 1;
			else
				c = 0;
			a[i] %= 2;
		}
	}
	
	void display(){
		for(int i = 0; i < nBits; i++)
			System.out.print(a[i]);
		System.out.print("\t\t");
		for(int i = 0; i < nBits; i++)
			System.out.print(q[i]);
		System.out.print("\t\t" + q_1 + "\n");
	}
	
	void boothsMultiplication(){
		if(q[nBits-1] == 0 && q_1 == 1){
			addition(m); //A = A+M
		}
		else if(q[nBits-1] == 1 && q_1 == 0){
			addition(m_); //A = A-M
		}
		arithmeticShiftRight();
	}
	
	int[] twosComplement(int[] y){
		int tmp = 0;
		for(int i = y.length-1; i >= 0; i--){
			if(tmp == 0 && y[i] == 0){
				continue;
			}
			else if(tmp == 0 && y[i] == 1){
				tmp = 1;
				continue;
			}
			if(y[i] == 0)
				y[i] = 1;
			else if(y[i] == 1)
				y[i] = 0;
		}
		return y;
	}
	
	void sendResult(){
		int[] result = new int[2 * nBits];
		int i;
		for(i = 0; i < nBits; i++)
			result[i] = a[i];
		int tmp = i;
		for(i = 0; i < nBits; i++, tmp++)
			result[tmp] = q[i];
		
		//binary to decimal
		if(flag == 1)
			result = twosComplement(result);
		
		String resultString = "";
		for(int j = 0; j < result.length; j++)
			resultString += String.valueOf(result[j]);
		
		int resultInt = Integer.parseInt(resultString, 2);
		
		if(flag == 1)
			resultInt = -resultInt;
		
		System.out.println("---------------------------------------\nResult is: " + resultInt);
		
		try {
			dos.writeUTF(String.valueOf(resultInt));
			dos.close();
			dis.close();
			s.close();
			ss.close();
		} catch (IOException e) {}
	}
	
	public static void main(String[] args) {
		MyServer ms = new MyServer();
		ms.establishConnection();
		ms.getData();
		for(int i = 0; i < ms.nBits; i++){
			ms.boothsMultiplication();
			ms.display();
		}
		ms.sendResult();
	}
}

/* OUTPUT
Number 1: 00100
Number 2: 00101
---------------------------------------
A		Q		Q-1
---------------------------------------
11110		00010		1
00001		00001		0
11110		10000		1
00001		01000		0
00000		10100		0
---------------------------------------
Result is: 20
*/
