from flask import Blueprint, request, redirect, url_for

from aux_functions import modify30DayLoginCookie

user_site = Blueprint('user_site', __name__)

@user_site.route('/home/')
def user_home():
	if 'previous_login' not in request.cookies:
		return redirect(url_for('login'))
	return modify30DayLoginCookie(request, render_template('user_home.html'))