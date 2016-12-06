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
username = sentData['username'].value

conn = mysql.connector.connect(user='DCC', password='abcd', database='Ocean')
cursor = conn.cursor()
# query = "SELECT GROUP_CONCAT(MessageID separator ', ') FROM Favorites where Uname  = '"+username+"';"
query = "SELECT * FROM Messages WHERE mID IN (SELECT MessageID FROM Favorites WHERE Uname='"+username+"');" #UNSANITIZED UNTIL FURTHER NOTICE
cursor.execute(query)
result = cursor.fetchall();
# result = result[0]
conn.close()

# formattedResult = ""
# for column in result:
# 	formattedResult += str(column)
# 	formattedResult += ","
# formattedResult = formattedResult[:-1]
#Format into comma seperated list

print("Content-type: text/html\n\n")
print(json.dumps(result))
