#!/usr/bin/env python



#CC
import cgitb
import cgi
import mysql.connector
import hashlib
import datetime

def insert_user(username, password):
    salt = str(datetime.datetime.now())

    hasher = hahlib.sha256()
    hasher.update(password)
    hasher.update(salt)
    encrypted = hasher.hexdigest()

    conn = mysql.connector.connect(user='webConn', password='pass',
                               host='127.0.0.1',
                               database='WebApp')
    cursor = conn.cursor()
    add_user = ("INSERT INTO users"
            "(username, pass, salt)"
            "VALUES (%s, %s, %s)")
    userToAdd = (username, password, salt)

    cursor.execute(add_user, userToAdd)
    conn.commit()

    cursor.close()
    conn.close()



def dupliCheck(username):
    conn = mysql.connector.connect(user='webConn', password='pass',
                               host='127.0.0.1',
                               database='WebApp')
    cursor = conn.cursor()

    a = cursor.execute("SELECT * FROM pizza_orders WHERE username=?", [username])
    if (len(a) >= 1):
        return false
    return true
    
def redir():

    toLog = "/login.html"

    print 'Content-Type: text/html'
    print 'Location: %s' % toLog
    print
    print '<html>'
    print '  <head>'
    print '    <meta http-equiv="refresh" content="0;url=%s" />' % toLog
    print '    <title>Success!</title>'
    print '  </head>' 
    print '  <body>'
    print '    You have successfully signed up, and will now be sent to login... <a href="%s">Click here if you are not redirected</a>' % toLog
    print '  </body>'
    print '</html>'



#Code here
form = cgi.FieldStorage()
    
username = form['username'].value
password = form['password'].value

if(dupliCheck(username)):
    insert_user(username, password)
    redir()

else:
    
    tryAgain = "/create_account.html?status=failed"
    print 'Location: %s' % tryAgain
   





