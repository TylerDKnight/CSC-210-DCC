#!/usr/bin/python2.7
#HASHBANG CHANGED FOR LINUX COMPATIBILITY

import cgi
import cgitb
import mysql.connector
import Cookie
import hashlib
import datetime
import os
import cookie_handler
import json

cgitb.enable()

sentData = cgi.FieldStorage()
messageID = sentData['messageID'].value
username = cookie_handler.readLoginCookieHeader()


conn = mysql.connector.connect(user='DCC', password='abcd', database='Ocean')
cursor = conn.cursor()
query = "DELETE FROM Favorites WHERE MessageID="+messageID+";"
cursor.execute(query)
conn.commit()
conn.close()


"""INSERT INTO Messages
        (Data, Title, Posttime, UnameSent)
        VALUES (%s, %s, %s, %s)"""



print "Content-type: text/html\n\n"


