<%@page import="java.io.*,java.net.*"%>
<html>
	<center>
	<h1>Booths Multiplication</h1>
	<h2>----------------RESULT----------------</h2>
	<h3>
	<%
		try{
			String str1 = request.getParameter("number1");
			String str2 = request.getParameter("number2");
			String str3 = request.getParameter("numBits");
			Socket s = new Socket("localhost",8888);
			DataInputStream dis = new DataInputStream(s.getInputStream());
			DataOutputStream dos = new DataOutputStream(s.getOutputStream());

			dos.writeUTF(str1);
			dos.writeUTF(str2);
			dos.writeUTF(str3);
			dos.flush();

			try{
				while(dis.available() == 0){
					String result = (String)dis.readUTF();
					out.println("Result of " + str1 + " * " + str2 + " = " + result);
	%>
					<form action="client.jsp"> <br>
					<input type="submit" value="<-- Back">
	<%
					dis.close();
				}
			}catch(Exception e){}
			dos.close();
			s.close();
		} catch(Exception e){
			out.println("Please Connect to Server...");
		}
	%>


	</h3>
	</center>
</html>