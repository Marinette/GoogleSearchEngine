<!DOCTYPE html>
<html>
	<head>
    <title> Roast </title>
		<link rel="stylesheet" href="/static/homepage.css">
	</head>

	<body>

	<form action ="/logout" method="PUT">
		<p><input value = "Sign Out" type="submit" class = "button"/></p>
	</form>

		<div id = "page">
			<div id = "name">
				<img src="/static/logo.png" alt="Logo" >
			</div>
			<form action ="/search" method="post">
				<p><input class = "search" name="keywords" placeholder = "ask me anything..." type="text"/></p>
				<p><input value = "Search" type="submit" class = "button"/></p>
			</form>
		</div>
		<br>
		<p>
			{{!history}}
		</p>
		<p>
			{{!table}}
		</p>

	</body>

</html>
