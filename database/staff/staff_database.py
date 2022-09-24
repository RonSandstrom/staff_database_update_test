from threestep.database.c_database_connect import DatabaseConnect
from threestep.database.c_table import Table
from threestep.cache.c_singleton import Singleton
from threestep.result.c_result import Result
from threestep.std_logging.logs import logger

from database.staff.c_staff_master_list_table import StaffMasterList


@Singleton
class StaffDatabase(object):
    def __init__(self):
        self.staff = DatabaseConnect(application='staff', dictionary=True)
        self.master_list_table: Table = self.automation.db.table(table_name='master_list', dictionary=True)

    def show_result(self, result: Result = Result(-1)):
        if result.is_ok():
            for row in result.data:
                s_row: StaffMasterList = StaffMasterList(row=row)
                logger.info(s_row)

    def get_staff_member(self, user_name) -> Result:
        first_name = ''
        last_name = ''
        parts = user_name.split(' ')
        if len(parts) == 2 :
            first_name = parts[0]
            last_name = parts[1]
        return self.master_list_table.fetch_many(where=f"`first_name` = '{first_name}' and `last_name` = '{last_name}'")