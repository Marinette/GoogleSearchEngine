<!DOCTYPE html>
<html>
	<head>
    <title> Roast </title>
		<link rel="stylesheet" href="/static/homepage.css">
	</head>

	<body>

	<form action ="/login" method="GET">
		<p><input value = "Sign In" type="submit" class = "button"/></p>
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

	</body>

</html>
