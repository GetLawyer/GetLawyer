#!/usr/bin/env python

import MySQLdb, cgi, cgitb
db = MySQLdb.connect( host = "localhost", user="root", passwd="root", db="GetLawyer")
cgitb.enable(display=0, logdir="cgilog.txt")

print "Content-type: text/html"
print
print '''
<html>
<title>Search</title>
<body>
'''

form = cgi.FieldStorage()
areas = form.getvalue('areas')

cur = db.cursor()

cur.execute("SELECT * FROM lawyers WHERE areas LIKE '%s'" % ("%" + areas + "%"))

print "<br>"
for row in cur.fetchall():
	print row[1]
	print row[2]
	print "<br>"
	print row[3]
	print "<br>"
	print row[5]
	print row[4]
	print "<br>"
	print row[6]
	print "<br>"
	print row[10]
	print "<br>"
	print"<br>"
print "</body>"
print "</html>"

