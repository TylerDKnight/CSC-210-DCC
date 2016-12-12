

<header>
	<div id="ocean-logo">
		<object id="ocean-logo" type="image/svg+xml" data="images/richie_logo1.svg">
			<img id="ocean-logo-fallback" src="images/richie_logo1.png" alt="Ocean Logo">
		</object>
	</div> <!-- ocean-logo -->
	<nav>
		<ul>
			<?php
			if (!empty($_GET['act'])) {
				setcookie("previous_login", " ", time() - 3600);
				header("Refresh:0");
			} else { }
 			?>
			 <form action="index.php" method="get">
				<input type="hidden" name="act" value="run">
				<input type="submit" value="Logout">
			 </form>
			<li><a id="nav-learn-more" href="learn_more.php">Learn More</a></li>
		</ul>
	</nav>
</header>
<body>
<!--
	<h1>Send a message!</h1>
	<form id="messageSub" method="post" action="cgi-bin/subMessage.py">
			<input type="text" name="message" id="message" class="vertical-form-input">
			<input type="submit" value="SEND">
		</form>
		-->
	<script>
		$(function() {
			$('#messageSub').submit(function(event) {
				if ($('#message').val() === "") {  // field is empty
					$('#message-error').text("Message field is empty.");
					event.preventDefault();  // stop form from being submitted
				} else {
					$('#message-error').text("");
				}
			});
		});
	</script>
</body>

