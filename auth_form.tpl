%# Template for generating authorization form

<!DOCTYPE html>
<html>

<head>
  <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">
</head>

<body>
<form class="form-horizontal" action="login" method="post">
  <div class="control-group">
    <label class="control-label" for="inputEmail">Hostname</label>
    <div class="controls">
      <input type="text" id="host" name="host" placeholder="Hostname">
    </div>
  </div>
  <div class="control-group">
    <label class="control-label" for="inputEmail">Username</label>
    <div class="controls">
      <input type="text" id="username" name="username" placeholder="Username">
    </div>
  </div>
  <div class="control-group">
    <label class="control-label" for="inputPassword">Password</label>
    <div class="controls">
      <input type="password" id="password" name="password" placeholder="Password">
    </div>
  </div>
  <div class="control-group">
    <div class="controls">
      <button type="submit" class="btn">Sign in</button>
    </div>
  </div>
</form>
</body>

</html>