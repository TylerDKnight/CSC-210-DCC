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

conn = mysql.connector.connect(user='DCC', password='abcd', database='Ocean')
cursor = conn.cursor()
query = "SELECT Title, Data, UnameSent, Posttime FROM Messages ORDER BY RAND() LIMIT 1"
cursor.execute(query)
result = cursor.fetchall()
result = result[0]
jsonreturn = {"Title": result[0], "Data": result[1], "UnameSent": result[2], "Posttime": result[3]}

conn.close()



# loopCounter = 0;
# while "\"" in result or "\'" in result: #Cleanse results of quotes
# 	result[result.index("\"")] = "\\"+"\""
# 	result[result.index("\'")] = "\\"+"\'"
# 	if loopCounter > len(result):  #Basic inf loop failsafe
# 		break;

#formattedResult = ""
#for column in result:
#	formattedResult += str(column)
#	formattedResult += ","
#formattedResult = formattedResult[:-1]
#Format into comma seperated list

print ("Content-type: text/html\n\n")
print json.dumps(jsonreturn)
