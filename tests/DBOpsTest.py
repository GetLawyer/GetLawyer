import unittest
import os
import sys
sys.path.insert(0, os.path.abspath('../site-root/cgi-bin/'))
import DBOps

# Automated tests for DBOps module
# Just basic checks to make sure the database connection is working
# and returning data that looks good

class DBOpsTest(unittest.TestCase):
    def test_connect(self):
        db = DBOps.dbConnect()
        self.assertTrue(db is not None,'Bad database handle')

    def test_searchStandard(self):
        areas = 'debt'
        lawyers = DBOps.searchStandard(areas)
        # print lawyers
        self.assertTrue(len(lawyers) > 0,'Standard search failed to return any results')

    def test_searchAdvanced(self):
        city = 'New York'
        state = 'NY'
        lawyers = DBOps.searchAdvanced(city,state)
        # print lawyers
        self.assertTrue(len(lawyers) > 0,'Advanced search failed to return any results')

    def test_addClient(self):
        db = DBOps.dbConnect()
        count = db.cursor()
        count.execute('SELECT * FROM clients')
        oldCount = len(count.fetchall())
        # print oldCount
        DBOps.addClient('Foo Bar','test@example.com','password','Los Angeles','CA')
        count.execute('SELECT * FROM clients')
        newCount = len(count.fetchall())
        # print newCount
        self.assertTrue(newCount == (oldCount + 1),'Adding a client failed to modify database')

    def test_addLawyer(self):
        db = DBOps.dbConnect()
        count = db.cursor()
        count.execute('SELECT * FROM lawyers')
        oldCount = len(count.fetchall())
        # print oldCount
        DBOps.addLawyer('Foo Bar','Qux Legal','404 Baz St','404 404 8080','bar@example.com','debt, injury, Metasyntactic variables','','Seattle','AK','Unlicensed','password')
        count.execute('SELECT * FROM lawyers')
        newCount = len(count.fetchall())
        # print newCount
        self.assertTrue(newCount == (oldCount + 1),'Adding a lawyer failed to modify database')

if __name__ == "__main__":
    unittest.main()
