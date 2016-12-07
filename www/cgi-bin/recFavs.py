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
query = "SELECT Data, Title, Posttime, UnameSent, mID FROM Messages WHERE mID IN (SELECT MessageID FROM Favorites WHERE Uname='test4');" #UNSANITIZED UNTIL FURTHER NOTICE
cursor.execute(query)

result = cursor.fetchall()
jsonreturn = dict()
# for i in range(len(result)):
# 	jsonreturn[str(i)+"|Data"] = result[i][0]
# 	jsonreturn[str(i)+"|Title"] = result[i][1]
# # result = result[0]
for i in range(len(result)):
	jsonreturn[str(i)] = {"Data": result[i][0], "Title": result[i][1], "Posttime": result[i][2], "UnameSent": result[i][3], "mID": result[i][4]}
conn.close()

print "Content-type: application/json\n\n"
print json.dumps(jsonreturn)



