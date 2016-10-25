'''
Script forming the page if user successfully authenticated.

There shouldn't be a need to import cgi or cgitb because the scripts using it should.
'''
import datetime

cookie_time_string = "%a, %d-%b-%Y %T UTC"  # format for cookie expiration time

def generateUserAccountPage(username):
	print 'Content-type: text/html'
	print '''\r\n\r\n
<html lang="en-us">
<head>
	<meta charset="utf-8">
	<meta name="author" content="DCC, Inc.">
	<link rel="stylesheet" href="css/dccstyles.css">
	<link rel="shortcut icon" href="images/favicon.png">
	'''
	print '	<title>' + username + ' - Home</title> </head>'
	print '<body>'
	print '<h1>Welcome, ' + username + '!</h1> </body> </html>'
