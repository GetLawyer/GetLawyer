#!/usr/bin/env python

import MySQLdb, cgi, cgitb
db = MySQLdb.connect( host = "localhost", user="root", passwd="root", db="GetLawyer")
cgitb.enable(display=0, logdir="cgilog.txt")

print "Content-type: text/html"
print
print '''
<html>
<head>
<title>New Lawyer</title>
</head>
<body>
Success!
<br>
</body>
</html>
'''




form = cgi.FieldStorage()
name = form.getvalue('name')
organization = form.getvalue('organization')
address = form.getvalue('address')
telephone = form.getvalue('telephone')
email = form.getvalue('email')
areas = form.getvalue('areas')
bio = form.getvalue('bio')
city = form.getvalue('city')
statecode = form.getvalue('statecode')
license = form.getvalue('license')
password = form.getvalue('password')

cur = db.cursor()
cur.execute("INSERT INTO lawyers (name,organization,address,telephone,email,areas,bio,city,statecode,license,password) VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (name, organization, address, telephone, email, areas, bio, city, statecode, license, password)) 

