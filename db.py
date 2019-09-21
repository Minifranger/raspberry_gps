import sqlite3
import loggers


class MetaDatabase(object):

    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()

    def execute(self, sql):
        loggers.logger.info("Executing query {sql}".format(sql=sql))
        return self.cursor.execute(sql)

    def create_table(self, table):
        loggers.logger.info("Creating sql table {name}".format(name=table.name))
        self.execute("CREATE TABLE if not exists {name} ({schema})".format(name=table.name, schema=table.schema))

    def delete_table(self, table):
        self.execute("DROP TABLE {name}".format(name=table.name))

    def list_tables(self):
        return self.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()


class MetaTable(object):

    def __init__(self, name, schema):
        self.name = name
        self.schema = schema
