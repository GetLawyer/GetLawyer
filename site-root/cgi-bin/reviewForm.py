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
#find another way to get this info name = form.getvalue('clientID')
#email = form.getvalue('lawyerID')
#password = form.getvalue('anonymous')
rating = form.getvalue('rating')
title = form.getvalue('title')
content = form.getvalue('content')

print "<h2>Hello %s</h2> your from %s<br>" % (name, city)

cur = db.cursor()
insrt = db.cursor()
insrt.execute("INSERT INTO reviews (clientID,lawyerID,anonymous,rating,title,content) VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\,\"%s\")" % (client, lawyer, anonymous, rating, title, content)) 

cur.execute("SELECT * FROM clients")
for row in cur.fetchall():
	print row
	print "<br>"


print'''
</body>
</html>
'
