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
        print lawyers
        self.assertEquals(len(lawyers) > 0,'Standard search failed to return any results')

    def test_searchAdvanced(self):
        city = 'New York'
        state = 'NY'
        lawyers = DBOps.searchAdvanced(city,state)
        print lawyers
        self.assertEquals(len(lawyers) > 0,'Advanced search failed to return any results')

    def test_addClient(self):
        db = dbConnect()
        count = db.cursor()
        oldCount = count.execute('SELECT COUNT(*) FROM lawyers')
        print oldCount
        addClient('Foo Bar','test@example.com','password','Los Angeles','CA')
        newCount = count.execute('SELECT COUNT(*) FROM lawyers')
        print newCount
        self.assertEquals(1==1,'Adding a client failed to modify database')


if __name__ == "__main__":
    unittest.main()
