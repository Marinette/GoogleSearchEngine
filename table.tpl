<!DOCTYPE html>
<html>
	<head>
    <title> Results </title>
		<link rel="stylesheet" href="/static/style.css">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
	</head>
	<header>
		<div class="pull-right not_too_right">
			<div class="dropdown">
				<button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">
					<div class="profilePic">
						<img src={{!profilePicture}} alt=" "></div>
					<span class="caret"></span>
				</button>
				<ul class="dropdown-menu dropdown-menu-right">
					<li><a href="#"> Hi {{!Name}}, </a></li>
					<li><a href="#">{{!Email}}</a></li>
					<li><a href="/logout"> Log Out</a></li>
				</ul>
			</div>
		</div>
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
