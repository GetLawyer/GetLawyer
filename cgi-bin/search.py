#!/usr/bin/env python

import MySQLdb, cgi, cgitb
db = MySQLdb.connect( host = "localhost", user="root", passwd="root", db="GetLawyer")
cgitb.enable(display=0, logdir="cgilog.txt")

print "Content-type: text/html"
print
print '''
<html>
<title>New User</title>
<p> Hello World</p>
<body>
'''

form = cgi.FieldStorage()
city = form.getvalue('city')
state = form.getvalue('statecode')

cur = db.cursor()


#case 1: only city
if city != 'NONE' and state = 'NONE':
	cur.execute(	
#case 2: only city
else if city = 'NONE' and state != 'NONE':
	cur.execute(
#case 3: both
else if city != 'NONE' and state != 'NONE':
