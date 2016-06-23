#!/usr/bin/env python

import MySQLdb, cgi, cgitb
db = MySQLdb.connect( host = "localhost", user="root", passwd="root", db="GetLawyer")
cgitb.enable(display=0, logdir="cgilog.txt")

print "Content-type: text/html"
print
print '''
<html>
<title>New User</title>
'''




form = cgi.FieldStorage()
name = form.getvalue('name')
email = form.getvalue('email')
password = form.getvalue('password')
city = form.getvalue('city')
statecode = form.getvalue('statecode')

cur = db.cursor()
cur.execute("INSERT INTO clients (name,email,password,city,statecode) VALUES (%(name)s,%(email)s,%(password)s,%(city)s,%(statecode)s)") 

cur.execute("SELECT * FROM clients")
for row in cur.fetchall():
	print row[0]

