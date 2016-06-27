# GetLawyer

A user-friendly attorney search engine.

Powered by Bootstrap, SQL, and other aging technologies.

#### Build/Install instructions

**Database/Website setup**

Navigate to the `mySQL` directory and start MySQL:

    cd GetLawyer/mySQL/
    sudo mysql -u root -p

At the MySQL prompt, verify that there is not an existing GetLawyer database and create a new database.

    SHOW DATABASES;
    # if GetLawyer is present:
    DROP DATABASE GetLawyer;
    SOURCE create-all.sql;

In another terminal, start a web server:

    cd GetLawyer/site-root/
    python -m CGIHTTPServer 8000

Open `localhost:8000` in a browser to view the website.

**Building docs**

Python docs (server side code is Python) are managed via [Sphinx](http://www.sphinx-doc.org/).

To create HTML documentation, execute the following:

    cd GetLawyer/docs
    make html

PDF documentation (assuming you have LaTeX and assorted tools installed):

    cd GetLawyer/docs
    make latexpdf

Docs are output to the following paths:

    docs/_build/html/index.html (HTML)
    docs/_build/latex/GetLawyer.pdf (PDF)

**Running tests**

Tests are built using the Python `unittest` framework. The tests verify that the server side Python interacts correctly with the MySQL database. To run the tests, you must have already set up the database (see above).

    cd GetLawyer/tests
    python DBOpsTest.py
