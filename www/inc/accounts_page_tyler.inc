<body>
	<!--Simple account information from the stored cookie. For now, it's just the username.-->
	 <?php
		if(!isset($_COOKIE[$cookie_name])) {
    		echo "User info not found!";
		} else {
    		echo "Your username is: " . $_COOKIE[$cookie_name];
		}
	?>
	<br>
	<br>
	<button><a href="/testtheme.php">BACK</a></button>
</body>