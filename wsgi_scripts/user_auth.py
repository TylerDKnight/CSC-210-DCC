'''
This is a blueprint, which contains other functions for creating other pages.  It helps to properly separate
the app into different files in order to better keep track of where things are.
'''
from flask import request, Blueprint, redirect, url_for
import hashlib, datetime

user_auth = Blueprint('user_auth', __name__)

@user_auth.route('/login_processing/', methods = ['GET', 'POST'])
def login_processing():
	if request.method == 'POST':
		username = request.form['username']
		rawpswd = request.form['password']
		# look up salt here
		salt = None  # PLACEHOLDER
		# end of looking up salt
		hasher = hashlib.sha256()
		hasher.update(rawpswd)
		hasher.update(salt)
		encpswd = hasher.hexdigest()
		# look up the password here
		password = None  # PLACEHOLDER
		#end of looking up password

		# check password
		if password == encpswd:
			# redirect(url_for(''))
			pass
		else:  # login failed
			return redirect(url_for('login', failed = 'failed'))
	else:
		return redirect(url_for('login', failed = 'failed'))  # should default to failure if wrong type of data was sent


@user_auth.route('/uname_collision_check/')
def uname_collision_check():
	#
	# stuff to check for collisions goes here
	#
	if True: #and data.rowcount > 0  # just a placeholder
		return 'collision'
	else:
		return 'ok'



