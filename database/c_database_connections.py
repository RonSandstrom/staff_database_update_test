
from threestep.cache.c_singleton import Singleton
from threestep.database.c_database_connect import DatabaseConnect
from threestep.database.c_table import Table
from threestep.std_utility.c_datetime import DateTime


class DBConnection:
    def __init__(self, application, schema, table, dictionary=True):
        self.application = application
        self.schema = schema
        self.table = table
        self.last_connection = DateTime(init='now')

        self.mysql = DatabaseConnect(application=application, dictionary=dictionary)
        if schema is None:
            self.schema = self.mysql.db.schema
        else:
            # override the application schema
            self.schema = schema
            self.mysql.db.schema = schema

        self.table: Table = self.mysql.db.table(table_name=table, dictionary=True)


@Singleton
class DBC(object):
    def __init__(self):
        self.connections = {}

    def get_key(self, application = None , schema = None, table = None):
        if application is None or table is None:
            return None
        return f"{str(application)}-{str(schema)}-{str(table)}"

    def table(self, application = None , schema = None, table = None ):
        table: Table
        key = self.get_key(application, schema, table)
        assert(key is not None, "Table Request is missing application and or table name")

        if key not in self.connections:
            dc = DBConnection(application, schema, table)
            self.connections[key] = dc
        else:
            dc = self.connections.get(key)

        return dc.table





