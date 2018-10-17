<!DOCTYPE html>
<html>
	<head>
    <title> Results </title>
		<link rel="stylesheet" href="/static/table.css">
	</head>
	<header>
		<p>
			<img src="/static/logo.png" alt="Logo">
			<form action = "/search" method="post">
				<input class = "search" name="keywords" type="text"/>
				<input value = "Search" type="submit" class = "button"/>
			</form>
			<p>
				<form action = "/">
					<input value = "Back" type="submit" class = "button"/>
				</form>
			</p>
		</p>
	</header>
	<body>
		<p>
			<h4> Search for "{{!keyword}}" </h4>
		</p>
		<p>
			{{!table}}
		</p>
	</body>

</html>
