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
name = form.getvalue('name')
email = form.getvalue('email')
password = form.getvalue('password')
city = form.getvalue('city')
statecode = form.getvalue('statecode')

print "<h2>Hello %s</h2> your from %s<br>" % (name, city)

cur = db.cursor()
insrt = db.cursor()
insrt.execute("INSERT INTO clients (name,email,password,city,statecode) VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (name, email, password, city, statecode)) 

cur.execute("SELECT * FROM clients")
for row in cur.fetchall():
	print row
	print "<br>"


print'''
</body>
</html>
'''
