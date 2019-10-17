import unittest
from db import db
from os.path import isfile


class TestDB(unittest.TestCase):

    db_path = "data/dbs/test_db"
    table_name, table_schema = "test_table", "date text, lat float, lon float"

    def test_init(self):
        test_db = db.MetaDatabase(path=self.db_path)
        self.assertTrue(isfile(test_db.path))

    def test_del(self):
        test_db = db.MetaDatabase(path=self.db_path)
        test_db.__exit__(None, None, None)
        test_db._del()
        self.assertFalse(isfile(self.db_path))

    def test_create_table(self):
        test_db = db.MetaDatabase(path=self.db_path)
        test_table = db.MetaTable(name=self.table_name, schema=self.table_schema)
        test_db.create_table(test_table)
        self.assertTrue(self.table_name in [table for (table, ) in test_db.list_tables()])

    def test_delete_table(self):
        test_db = db.MetaDatabase(path=self.db_path)
        test_table = db.MetaTable(name=self.table_name, schema=self.table_schema)
        test_db.create_table(test_table)
        test_db.delete_table(test_table)
        self.assertFalse(self.table_name in [table for (table, ) in test_db.list_tables()])


if __name__ == '__main__':
    unittest.main()
