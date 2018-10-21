<!DOCTYPE html>
<html>

<head>
	<title> Roast </title>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
	<link rel="stylesheet" href="/static/homepage.css">
</head>

<body>

	<form action="/login" method="PUT">
		<p><input value="Sign In" type="submit" class="button" /></p>
	</form>

	<div id="page">
		<div id="name">
			<img src="/static/logo.png" alt="Logo">
		</div>
		<form action="/search" method="post">
			<p><input class="search" name="keywords" placeholder="ask me anything..." type="text" /></p>
			<p><input value="Search" type="submit" class="button" /></p>
		</form>
	</div>
	<br>

</body>

</html>
