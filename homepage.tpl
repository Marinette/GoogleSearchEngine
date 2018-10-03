<!DOCTYPE html>
<html>
	<head>
    <title> Searchy </title>
		<style>
		body {
		font-family: sans-serif;
		text-align: center;
		font-weight: bold;
		width: 1000px;
}
h1 {
		color: #4CAF50;
		font-size: 100px;
		text-align: center;
		font-weight: bold;
}
form {
    text-align: center;
}
input[type="text"] {
		border-width: 0px;
		border: solid #777777;
		width: 500px;
		height: 22px;
		font-size: 18px;
}
.counter {
	text-align: center;
}
.historyt {
	text-align: center;
}
.button {
	background-color: white; /* Green */
	border: solid #4CAF50;
	color: #4CAF50;
	padding: 10px 24px;
	text-align: center;
	text-decoration: none;
	display: inline-block;
	font-size: 16px;
	transition-duration: 0.4s;
}

.button:hover {
    background-color: #4CAF50; /* Green */
    color: white;
}

table {
	  font-family: sans-serif;
	  width: 50%;
	  border-color: black;
	  float: left;
  text-align: center;
}
			textarea {
	  			border: 1px solid #777777;
				padding: 10px;
				height: 300px;
				width: 500px;
	   			resize: none;
			}
		</style>
	</head>
	<body>
		<div id = "page">
			<div id="name">
				<h1>Searchy</h1>
			</div>
			<form action ="/" method="post">
				<p><input name="keywords" placeholder = "Enter keywords" type="text"/></p>
				<p><input value = "Search" type="submit" class = "button"/></p>
			</form>
		</div>

	</body>
</html>
