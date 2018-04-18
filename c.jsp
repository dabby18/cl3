<%@ page import="java.io.*, java.net.*" %>
<HTML>
   <BODY bgcolor="pink">
	 <%       
	 try
        {      
            Socket s=new Socket("localhost",8776);  
	    DataOutputStream dout=new DataOutputStream(s.getOutputStream());  
	    DataInputStream inSocket = new DataInputStream(s.getInputStream());
	    String str1 = request.getParameter("number1");
	    dout.writeUTF(str1);  
	    dout.flush(); 
	    int n = Integer.parseInt(str1);
	    for(int i=0;i<=n-1;i++)
	    {
	    	String name="num"+i;
	    	str1 = request.getParameter(name);
	    	dout.writeUTF(str1);  
	    	dout.flush(); 
	    }
            dout.flush(); 
	    String strr;
	    
	    try
	    {
		    while(inSocket.available() == 0)
		    {
		    	%>
		    	<br><br><br><center><font face="Times New Roman",size ="18">
		    	<%
		    	out.println("INPUT ARRAY    =>   ");
		    	strr=(String)inSocket.readUTF();
		    	out.print(strr);
		    	%>
		    	<br><br><br><br><br>
		    	<%
		    	out.println("SORTED ARRAY    =>  "); 
		    	strr=(String)inSocket.readUTF();
		    	out.print(strr);
			inSocket.close(); %> </center></font> <%   
		    }
            }
            catch(Exception e){}
            dout.close();  
            s.close();  
    	}
    	catch(ConnectException e)
    	{%>
    		Server not connected .............
    	<%	
    	}  
        %>
   </BODY>
</HTML>
