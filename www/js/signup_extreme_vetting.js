/*
This is meant to replace the scripts in the create_account.html file.
It both checks to see if a username is taken as the user types AND prevents the
form from being sent if the username is taken.

The type returned from the script is a plain utf-8 text word, either "collision" or "ok".
*/

$(function() {
	$('#username').on('input', function(event) {
		username_check(event, false);  // do not stop event if uname is taken
	});

	$('#password').on('input', function(event) {
		password_check(event, false, $('#password'));
	});

	$('#confirm-password').on('input', function(event) {
		password_check(event, false, $('#confirm-password'));
	});

	$('#account_info').submit(function(event) {
		username_check(event, true);  // stop event if uname is taken
		password_check(event, true, $('#password'));  // it does not matter which pswd field gets passed in
	});
});  // document ready


var username_check = function(event, preventDefault) {
	// check the username status when any key is pressed in the username field
	// allow the function to prevent the default of the event if necessary
	if ($('#username').val() === '') {
		$('#username-error').text('Username field is empty.');
		if (preventDefault === true) {
			event.preventDefault();
		}
	}

	else {
		var $uname_err = $('#username-error');
		$uname_err.text('');  // clear previous username error to check for new one
		$.ajax({  // perform ajax check
			url: '../cgi-bin/uname_collisions.py',
			data: {username: $('#username').val()},
			type: 'POST',
			dataType: 'text',
			success: function (data) {
				// data is to be either "collision" or "ok"
				if (data == 'collision') {  // put "already taken" message in html and optionally halt event
					$uname_err.text('Username is already taken.');
					if (preventDefault === true) {
						event.preventDefault();
					}
				}
			},
			error: function(request) {
				// this should be treated as a script error and should not ever occur in the finished product
				console.log('ERROR: Checking for username conflicts failed.');
				console.log('Request: %s', request.toString());
			}
		});  // ajax
	}
};


var containsRequiredChars = function(pswd, chars) {
	// where pswd is the password and chars a string containing required chars
	// checks if pswd contains ANY of the chars
	for (i=0; i<pswd.length; i++) {
		if (chars.indexOf(pswd.charAt(i)) != -1) {  // the selected char of pswd is required
			return true;
		}
	}
	return false;  // no required character has been found
};


var password_check = function(event, preventDefault, $field) {
	// allow for the function to prevent the default action for an event if possible
	// $field should be the jquery obj representing the field to check, either password or confirm-password

	var pswd = $field.val();
	var $pswd_err = $('#password-error');
	

	if (pswd === '') {
		$pswd_err.text('Password field is empty.');
		if (preventDefault === true) {
			event.preventDefault();
		}
	}

	else if (pswd.length < 8 || !containsRequiredChars(pswd, '!@#$%^&*()-_=+[]{}\\|"\':;<>,./?`~') ||
		!containsRequiredChars(pswd, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') || !containsRequiredChars(pswd,
			'abcdefghijklmnopqrstuvwxyz') || !containsRequiredChars(pswd, '1234567890')) {
			// is too short or lacks a character from any of the groups of required chars
		$pswd_err.text('Password must be at least 8 characters in length and contain one digit, one uppercase' +
			'letter, one lowercase letter and one special character (which can be any of ' +
				'!@#$%^&*()-_=+[]{}\\|"\':;<>,./?`~).');
		if (preventDefault === true) {
			event.preventDefault();
		}
	}
	else if ($('#password').val() != $('#confirm-password').val()) {  // password is correct but does not match confirmation
		$pswd_err.text('Password fields do not match.');
		if (preventDefault === true) {
			event.preventDefault();
		}
	}

	else $pswd_err.text('');  // everything is ok
};

