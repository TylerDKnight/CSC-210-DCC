<header>
	<div id="ocean-logo">
		<object id="ocean-logo" type="image/svg+xml" data="{{ url_for('static', filename='images/richie_logo1.svg') }}">
			<img id="ocean-logo-fallback" src="{{ url_for('static', filename='images/richie_logo1.png') }}" alt="Ocean Logo">
		</object>
	</div> <!-- ocean-logo -->
	<nav>
		<ul>
			<li><a id="nav-home" href="{{ url_for('login', failed = '') }}">Login</a></li>
			<li><a id="nav-messages" href=".">Messages</a></li>
			<li><a id="nav-conversations" href=".">Conversations</a></li>
			<li><a id="nav-logout" href=".">Log Out</a></li>
		</ul>
	</nav>
</header>

