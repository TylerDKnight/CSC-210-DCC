#!C:/Python27/python.exe

import cgi
import cgitb
import mysql.connector
import Cookie
import hashlib
import datetime
import os
import cookie_handler

cgitb.enable()


#get message data
messageInfo = cgi.FieldStorage()
content = messageInfo['message'].value
username = cookie_handler.readLoginCookieHeader()
conn = mysql.connector.connect(user='this', database='Ocean')
cursor = conn.cursor()
add_Message = ("""INSERT INTO Messages
        (Data, UnameSent)
        VALUES (%s, %s)""")
messageToAdd = (content, username)

cursor.execute(add_Message, messageToAdd)
conn.commit()

cursor.close()
conn.close()

print("Content-type: text/html\n\n")
print("Message Submitted")
