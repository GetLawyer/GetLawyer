#!/user/bin/env python
import MySQLdb

# NEVER EVER STORE PASSWORDS IN A VCS orother public-accesible location!!
db = MySQLdb.connect( host="localhost", # or web address for the db
			user="n8",	# db username
			passwd="test",
			db="Lab")	# name of database

print "Content-type: text/html"
print
print "<html>"
print "<title>Test CGI</title>"
print "<p>Hello World</p>"


# first must create a CUrsor object
cur = db.cursor()

# run execute on cursor with you SQL
cur.execute("SELECT * FROM Dept")

for row in cur.fetchall() :
	print row[0]
print "Done"

cur.execute ("SELECT * FROM store")
print "<table border=1>"
for row in cur.fetchall():
	print "<tr><th>"
	print row[0]
	print "</th><td>"
	print row[1]
	print "</td>"
	print "</tr>"
print "</table>"

import cgi, cgitb
cgitb.enable(display=0, logdir="cgilog.txt")

form = cgi.FieldStorage()
name = form.getvalue('name')
product = form.getvalue('product')

print "<h2>Hello %s</h2> You want to buy %s" % (name, product)
