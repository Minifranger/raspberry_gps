import unittest
from db import db
from os.path import isfile


class TestDB(unittest.TestCase):

    db_path = "data/dbs/test_db"
    table_name, table_schema = "test_table", "date text, lat float, lon float"

    def test_init(self):
        test_db = db.MetaDatabase(path=self.db_path)
        self.assertTrue(isfile(test_db.path))

    def test_create_table(self):
        test_db = db.MetaDatabase(path=self.db_path)
        test_table = db.MetaTable(name=self.table_name, schema=self.table_schema)
        test_table2 = db.MetaTable(name="test2", schema=self.table_schema)
        test_db.create_table(test_table)
        test_db.create_table(test_table2)
        print(test_db.list_tables())
        print(type(test_db.list_tables()[0]))
        self.assertTrue(self.table_name in [table for (table, _) in test_db.list_tables()])

    def test_delete_table(self):
        test_db = db.MetaDatabase(path=self.db_path)
        self.assertTrue(isfile(test_db.path))


if __name__ == '__main__':
    unittest.main()
