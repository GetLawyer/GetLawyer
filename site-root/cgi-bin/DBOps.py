"""This module provides a set of standardized database operations for GetLawyer web pages. These are called by other routines in order to populate dynamic pages or register users."""

__docformat__ = 'reStructuredText'

# Import modules for communicating with MySQL database and managing CGI server calls
import MySQLdb, cgi, cgitb

def dbConnect():
    """returns database handle

    Connect to the database and enable CGI error handling. Used internally by the other functions.
    """
    # Get a handle to our database (@TODO remove password for production)
    db = MySQLdb.connect( host = "localhost", user="root", passwd="root", db="GetLawyer")
    # Log CGI error handling
    cgitb.enable(display=0, logdir="cgilog.txt")
    return db

def searchStandard(areas):
    """returns a list of tuples or an empty list

    Find all attorneys matching the specified areas and return as a list of tuples. If there are no records returned, returns an empty list

    :param areas: area keywords to search with
    :type areas: string

    **Notes**:
    Note that the "LIKE" operator in MySQL may not be the appropriate method of accomplishing a keyword search.
    """
    db = dbConnect()
    cur = db.cursor()
    cur.execute("SELECT * FROM lawyers WHERE areas LIKE '%s'" % ("%" + areas + "%"))
    return cur.fetchall()

def searchStandardPreamble():
    """returns a list of areas

    Retrieve a list of areas from a query

    **Notes**:
    At present, this function does not validate or sanitize inputs.
    """
    form = cgi.FieldStorage()
    return form.getvalue('areas')

def searchAdvanced(city,state):
    """returns a list of tuples or an empty list

    Find all attorneys matching the search criteria and return as a list of tuples. If there are no records returned, returns an empty list

    :param city: the city to search in
    :param state: the two-letter statecode to search in
    :type city: string
    :type state: string

    **Notes**:
    For development/testing purposes, this function only checks the statecode right now
    """
    db = dbConnect()
    cur = db.cursor()
    """@TODO: change to index both state and city"""
    cur.execute("SELECT * FROM lawyers WHERE statecode = '%s'" % (state))
    return cur.fetchall()

def searchAdvancedPreamble():
    """returns a tuple with city and statecode

    Return city and statecode from a query

    **Notes**:
    At present, this function does not validate or sanitize inputs.
    """
    form = cgi.FieldStorage()
    city = form.getvalue('city')
    state = form.getvalue('statecode')
    return (city,state)

def regClient():
    """returns nothing

    Retrieve client registration data input via CGI fields, then add a client

    **Notes**:
    At present, this function does not validate or sanitize inputs.
    """
    form = cgi.FieldStorage()
    name = form.getvalue('name')
    email = form.getvalue('email')
    password = form.getvalue('password')
    city = form.getvalue('city')
    statecode = form.getvalue('statecode')
    addClient(name,email,password,city,statecode)

def addClient(name,email,password,city,statecode):
    """returns nothing

    Add data in the MySQL database as a new client entry.

    :param name: client name
    :param email: client email
    :param password: client password
    :param city: client city
    :param statecode: client two-letter statecode
    :type name: string
    :type email: string
    :type password: string
    :type city: string
    :type statecode: string

    **Notes**:
    Missing fields are not allowed.
    """
    db = dbConnect()
    insert = db.cursor()
    insert.execute("INSERT INTO clients (name,email,password,city,statecode) VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (name, email, password, city, statecode))

def regLawyer():
    """returns nothing

    Retrieve attorney registration data input via CGI fields and add a lawyer.

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
    addLawyer(name,organization,address,telephone,email,areas,bio,city,statecode,license,password)

def addLawyer(name,organization,address,telephone,email,areas,bio,city,statecode,license,password):
    """returns nothing

    Add data in the MySQL database as a new lawyer entry.

    :param name: attorney name
    :param organization: attorney organization/firm
    :param address: attorney address
    :param telephone: attorney telephone number
    :param email: attorney email
    :param areas: areas of practice
    :param bio: short biography
    :param license: legal license reference
    :param password: attorney password
    :param city: attorney/firm city
    :param statecode: attorney two-letter statecode
    :type name: string
    :type organization: string
    :type address: string
    :type telephone: string
    :type email: string
    :type areas: string
    :type bio: string
    :type license: string
    :type password: string
    :type city: string
    :type statecode: string

    **Notes**:
    Missing fields are not allowed.
    """
    db = dbConnect()
    cur = db.cursor()
    cur.execute("INSERT INTO lawyers (name,organization,address,telephone,email,areas,bio,city,statecode,license,password) VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (name, organization, address, telephone, email, areas, bio, city, statecode, license, password))
