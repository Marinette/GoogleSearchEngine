<!DOCTYPE html>
<html>
	<head>
    <title> Results </title>
		<link rel="stylesheet" href="/static/table.css">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
	</head>
	<header>
		<img src = {{!profilePicture}} alt = {{!profilePicture}}>
		<h1>{{!Name}}</h1>
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
		<form action ="/logout" method="PUT">
			<p><input value = "Sign Out" type="submit" class = "button"/></p>
		</form>
		<p>
			<h4> Search for "{{!keyword}}" </h4>
		</p>
		<p>
			{{!table}}
		</p>
	</body>

</html>
