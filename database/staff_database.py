from threestep.database.c_database_connect import DatabaseConnect
from threestep.database.c_table import Table
from threestep.cache.c_singleton import Singleton


@Singleton
class StaffDatabaseTables(object):
    def __init__(self):
        self.staff = DatabaseConnect(application='staff', dictionary=True)
        self.master_list_table: Table = self.automation.db.table(table_name='master_list', dictionary=True)


