from flask import make_response
from datetime import datetime, timedelta

def modify30DayLoginCookie(request, rendered_template, add = True, addIfNotExists = False):
	''' returns a response containing a 30-day cookie keeping the user logged in
	the parameters are:
	1. a request which may or may not contain a cookie ('previous_login')
	2. a template rendered using the render_template function included in flask
	3. a boolean indicating whether the cookie is to be added or removed in the operation
	4. a boolean indicating whether the cookie should be added if not already in request

	The defaults should be sufficient to a standard cookie-driven replacement for render_template:
	the function, if supplied only with request and rendered_template, should renew the cookie
	if it already exists and do nothing otherwise.
	'''
	resp = make_response(rendered_template)

	exp_time = datetime.utcnow()
	if add == True:  # add the cookie
		if addIfNotExists == False:  # must check to see if cookie exists
			if 'previous_login' not in request.cookies:
				return resp  # response returned without adding cookie
		exp_time = exp_time + timedelta(30)
	else:  # remove the cookie
		exp_time = exp_time - timedelta(30)
		# cookie will immediately be removed since it expired 30 days ago

	resp.set_cookie('previous_login', value=user, expires=exp_time)
	return resp