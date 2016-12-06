

<header>
	<nav>
	</nav>
</header>
<body>
<div class="container-fluid">
  <div class="row content">
    <div class="col-sm-3 sidenav">
      <h1>Ocean</h1>
      <ul class="nav nav-pills nav-stacked">
        <li class="active"><a data-toggle="pill" href="#myaccount">My Account</a></li>
        <li><a data-toggle="pill" href="#favoritebottles">Favorite Bottles</a></li>
        <li><a data-toggle="pill" href="#chat">Chat</a></li>
        <li><a data-toggle="pill" href="#feed">Bottle Feed</a></li>
      </ul><br>

	<select id="menu-links">
		<option value="/testtheme.php"></option>
		<option value="/account_details.php">My account</option>
		<option value="">Send a bottle</option>
		<option value="">Recieve a bottle</option>
		<option value="https://lh3.googleusercontent.com/-2rj78ZwMvmA/AAAAAAAAAAI/AAAAAAAAAA8/fvpmcm1iITA/photo.jpg">DEARGODLETMELIVE</option>
		<option value="/learn_more.php">Learn More</option>
	</select>
	<button id="confirm_menu" class="button">Confirm</button>

      <div class="input-group">
        <input type="text" class="form-control" placeholder="Search Blog..">
        <span class="input-group-btn">
          <button class="btn btn-default" type="button">
            <span class="glyphicon glyphicon-search"></span>
          </button>
        </span>
      </div>
    </div>

    <div class="tab-content">
    	<div id="myaccount" class="tab-pane fade in active">
    		<h3>HOME</h3>
    		<p>Some content.</p>
    		<?php
    		if (!empty($_GET['act'])) {
    		setcookie("previous_login", " ", time() - 3600);
    		header("Refresh:0");
    		} else { }
    		?>
	    	<form action="index.php" method="get">
	    		<input type="hidden" name="act" value="run">
	    		<input type="submit" value="Logout" class="button" id="logout">
	    	</form>
    	</div>
    	<div id="favoritebottles" class="tab-pane fade">
    		<h3>Favorited bottles:</h3>
    		<div class="col-sm-9" id="fav-container">
    	</div>
    	<div id="chat" class="tab-pane fade">
    		<h3>Menu 2</h3>
    		<p>Some content in menu 2.</p>
    	</div>
    	<div id="feed" class="tab-pane fade">
    		<h4><small>RECENT POSTS</small></h4>
    		<div class="col-sm-9" id="post-container">
    		</div>
    	</div>
    </div>

  </div>
</div>


<footer class="container-fluid">
  <p>Footer Text</p>
</footer>


	<script type="text/javascript">
		function generatePost(title, author, content, date) {
			return "<hr>"+
					"<h2>"+title+"</h2>"+
					"<h5><span class=\"glyphicon glyphicon-time\"></span> Post by "+author+", "+date+".</h5>"+
					"<p>"+content+"</p>"+
					"<br><br>"
		}

		function retrievePost() {

		}

		$(function(){
			$("#confirm_menu").click(function() {

				var option = $("#menu-links option:selected").text(); //Retrieve menu option select when "Confirm" clicked
				var option_value = $("#menu-links option:selected").val();
				switch (option) { //Do various actions based on the value of the selection
					case "My account": //Redirect to accounts page
						window.location.href = option_value;
						break;
					case "Send a bottle": //Give focus to the send message bar
						$("#message").focus();
						break;
					case "Recieve a bottle": //Query recMessage.py to query database to get new posts
					$.ajax({
						type: "GET",
						url: "cgi-bin/recMessage.py",
						success: function(data, status) {
								var dataArray = data.split(",");
								var message = dataArray[0];
								var title = dataArray[1];
								var date = dataArray[2];
								var UNameTo = dataArray[3];
								var UnameSent = dataArray[4];
								var mID = dataArray[5];

								if (title == "") {
									title = "";
								}
								if (UnameSent == "") {
									UnameSent = "Anonymous";
								}

								var messageText = message;
								var titleText = title;
								var author = UnameSent;
								var dateText = date;
								$(generatePost(titleText, author, messageText, dateText)).prependTo("#post-container").hide().fadeIn('slow'); //Generate HTML to display recieved data
							},
							error: function(data, status) {
								alert("Unable to complete request.");
							}
						});
						break;
					case "DEARGODLETMELIVE": //O Great Roko, please have mercy
						window.location.href = option_value;
						break;
					case "Learn More": //Redirect to learn more
						window.location.href = option_value;
						break;
				}
			});


			$("#confirm_send").click(function() {
				var message, title = "";
				var anon = $('#anon').is(":checked");
				var timestamp = new Date().toLocaleString();
				message = $('#message').val(); //Extract textfield value when "Send!" clicked
				title = $('#title').val(); //Extract title textfield
				timestamp = timestamp.replace (/,/g, " "); //Replace ',' in datestring with ' '
				//For some reason, method won't send the timestamp only if message or title is blank
				//Temporary backup is to have the server insert the current time if it's not recieved /w POST data
				if (message+title != "") {
					$.ajax({
						type: "POST",
						url: "cgi-bin/subMessage.py",
						contentType: "application/x-www-form-urlencoded",
						data: {"message":message, "title":title, "timestamp":timestamp, "anon":anon},
						success: function(data, status) {
							$("#submission_status").html("Message cast!").css({"color":"#8F8"}).show().fadeOut(4000);
							$("#confirm_send").hide().fadeIn("slow");
						},
						error: function() {
							// alert("Unable to complete request.");
							$("#submission_status").html("Request failed!").css({"color":"#bf5454"}).show().fadeOut(4000);
							$("body").append(data); //REMOVE WHEN DONE TESTING; WILL ADD CGIB ERROR TO HTML BODY
						}
					});
				}
			});

			$("#logout").click(function(event) {
				if (confirm("Logout?")) {
					window.location.reload(true);
				} else {
					event.preventDefault();
				}
			});

			// Below has been written new for bootystrap since testtheme.php

			$("#favoritebottles").click(function(event) {
				var favoriteIDs;
				$.ajax({
					type: "GET",
					url: "cgi-bin/recFavs.py",
					dataType: "json",
					data: {"username":"test4"}, //USERNAME HARDCODED UNTIL FURTHER NOTICE
					success: function(data, status){
						$("body").append(data);
						// alert("UnJSON'd\n"+data);
						// console.log(data);
						// favoriteIDS = data[0];
						// alert("JSON'd\n"+favoriteIDs);
						// for id in favoriteIDs:
						// 	$(generatePost(titleText, author, messageText, dateText)).prependTo("#post-container").hide().fadeIn('slow');
					},
					error: function(data, status){
						alert("Unable to complete request.");
						console.log(status);
					}
				});
			});

		});
	</script>
</body>

