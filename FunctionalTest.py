import unittest;
import pymongo;
import sys;

class TestMongoStat(unittest.TestCase):

    def setUp(self):
        pass

    def test_import_pymongo(self):
        """Validate that pymongo db_driver is available in the path"""
        modules = sys.modules.keys()

        try:
            ix = modules.index("pymongo")
        except:
            ix = -1

        self.assertGreaterEqual(ix, 0)

if __name__ == "__main__":
    unittest.main()
