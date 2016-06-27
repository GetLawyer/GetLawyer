"""This module provides a set of standardized database operations for GetLawyer web pages. These are called by other routines in order to populate dynamic pages or register users."""

__docformat__ = 'reStructuredText'

# Import modules for communicating with MySQL database and managing CGI server calls
import MySQLdb, cgi, cgitb

# Get a handle to our database (@TODO remove password for production)
db = MySQLdb.connect( host = "localhost", user="root", passwd="root", db="GetLawyer")
# Log CGI error handling
cgitb.enable(display=0, logdir="cgilog.txt")

def searchStandard():
    """returns a list of tuples or an empty list

    Find all attorneys matching the search criteria and return as a list of tuples. If there are no records returned, returns an empty list

    **Notes**:
    At present, this function does not validate or sanitize inputs.
    Note that the "LIKE" operator in MySQL may not be the appropriate method of accomplishing a keyword search.
    """
    form = cgi.FieldStorage()
    areas = form.getvalue('areas')
    cur = db.cursor()
    cur.execute("SELECT * FROM lawyers WHERE areas LIKE '%s'" % ("%" + areas + "%"))
    return cur.fetchall()

def searchAdvanced():
    """returns a list of tuples or an empty list

    Find all attorneys matching the search criteria and return as a list of tuples. If there are no records returned, returns an empty list

    **Notes**:
    At present, this function does not validate or sanitize inputs.
    For development/testing purposes, this function only checks the statecode right now
    """
    form = cgi.FieldStorage()
    city = form.getvalue('city')
    state = form.getvalue('statecode')
    cur = db.cursor()
    """@TODO: change to index both state and city"""
    cur.execute("SELECT * FROM lawyers WHERE statecode = '%s'" % (state))
    return cur.fetchall()

def regClient():
    """returns nothing

    Retrieve client registration data input via CGI fields, then add this data in the MySQL database as a new client entry.

    **Notes**:
    At present, this function does not validate or sanitize inputs.
    """
    form = cgi.FieldStorage()
    name = form.getvalue('name')
    email = form.getvalue('email')
    password = form.getvalue('password')
    city = form.getvalue('city')
    statecode = form.getvalue('statecode')

    insert = db.cursor()
    insert.execute("INSERT INTO clients (name,email,password,city,statecode) VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (name, email, password, city, statecode))

def regLawyer():
    """returns nothing

    Retrieve attorney registration data input via CGI fields, then add this data in the MySQL database as a new lawyer entry.

    **Notes**:
    At present, this function does not validate or sanitize inputs.
    """
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
