<%@page import="java.io.*, java.net.*"%>
<html>
	<script>
		function clearFields()
		{
			document.getElementById("number1").value = "";
			document.getElementById("number2").value = "";
			document.getElementById("numBits").value = "";
		}
	</script>

	<body>
		<center>
		<h1>Booths Multiplication</h1>
		<form action="result.jsp">
		<p>Enter Number1: <input type="text" name="number1" id="number1"/>
		<p>Enter Number2: <input type="text" name="number2" id="number2"/>
		<p>Enter Number of Bits: <input type="text" name="numBits" id="numBits"/>
		<p><input type="submit" value="ENTER">
		<p><input type="button" value="Clear Fields" onclick="clearFields();">
		</center>
	</body>
</html>