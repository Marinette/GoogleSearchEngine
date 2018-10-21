<!DOCTYPE html>
<html>

<head>
	<title> Roast </title>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
	<link rel="stylesheet" href="/static/style.css">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>

<nav class="navbar navbar-light bg-light">
	<a class="navbar-brand" href="#">
		<div class = "profilePic">
    <img src= {{!profilePicture}} alt=""> </div>
  </a>

	<span class="navbar-brand mb-0 h1"> {{!Name}} </span>
</nav>

<body>
	<div class="container ">

		<div class="row h-100 justify-content-center align-items-center no-gutters">
			<div class="engineLogo">
				<img src="/static/logo.png" alt="Logo">
			</div>
		</div>

		<div class="row h-100 justify-content-center align-items-center">
			<class="col-6 justify-content-center">
				<form action="/search" method="post">
					<input class="form-control" name="keywords" placeholder="Search.." type="text" />
				</form>
		</div>
		<div class="row h-100 justify-content-center align-items-center">
			<h2>{{!history}}</h2>
			{{!table}}
		</div>
	</div>
</body>

</html>
