<%@ page import="java.io.*, java.net.*" %>
<HTML>
    <BODY bgcolor="lightgreen">
    <center>NUMBER OF ELEMENTS 
    <form action="c.jsp">
    <input name="number1" type="text" 
      value='<%=request.getParameter("number1")%>' /></center>
    <%       
	 
            String str1 = request.getParameter("number1");
            int n = Integer.parseInt(str1);
    %>
           
           <br><br><br><br> <center>ENTER ELEMENTS </center>
    <%
            for(int i=0;i<=n-1;i++)
            {
            	String str="num"+i;
     %>
            	<center><input type="text" name='<%=str%>' /></center>
            	
            	
    <%
            }
	
    %>
    <center><input type="submit" name="sub" id="sub" value="OK"/></center>
    </BODY>
</HTML>
