<!DOCTYPE html>

<html lang="en-us">

<head>
	<meta charset="utf-8">
	<meta name="author" content="DCC, Inc.">
	<link rel="stylesheet" href="css/dccstyles.css">
	<link rel="shortcut icon" href="images/favicon.png">
	<!-- add jquery -->
	<script src="https://code.jquery.com/jquery-1.10.2.js"></script>
	<title>Learn More</title>
</head>

<body>
	<?php include "inc/header_not_logged.inc"; ?>

	<div class="content">
		<h1>About Ocean</h1>

		<h2>The Foundations of Ocean</h2>
		<p>Ocean was created by DCC, Inc., a partnership of four young web developers: Richie, 
			Joey P., CC, and Ringo Starr.  The group decided to go about creating the site based on an
			idea for a completely anonymous, no-strings-attached messaging pool they called "Message 
			In A Bottle".  As the idea evolved, a favorites system was integrated into the user experience, and
			the project was renamed <span class="italic">theocean</span>.  However, at the advice of Justin
			Timberlake in the film <span class="italic">The Social Network</span>, the name was again
			changed to the sleeker, cleaner <span class="italic">Ocean</span>.</p>
	 

		<h2>Ocean's Features</h2>
		<p>Currently, Ocean allows any user to create an account and view their account information, and send messages (anonymous or not)
		"Out to Sea." These messages can be viewed and favorited by other users, and one can create a list of their own favorite messages, or "bottles," as we call them.</p>

	</div>  <!-- content -->
	<script src="js/nav-handler.js"></script>
	<script src="js/menu-highlighter.js"></script>  <!-- defines the function highlightMenuItemFromId(id_no_hashtag) -->

	<script>

	highlightMenuItemFromId("nav-learn-more");

	</script>  <!-- call the previously defined function -->

</body>

</html>
