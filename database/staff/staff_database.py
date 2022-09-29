from threestep.database.c_database_connect import DatabaseConnect
from threestep.database.c_table import Table
from threestep.cache.c_singleton import Singleton
from threestep.result.c_result import Result
from threestep.std_logging.logs import logger
from database.staff.c_master_list import MasterList

class DataHelper:
    """
    list out the contents of any database type
    """
    def show_result(self, class_type,  label: str, result: Result = Result(-1)):
        if result.is_ok():
            for row in result.data:
                s_row = class_type(row=row)
                logger.info(f"[{label}] Located record for [{s_row.user_name}] doc id = [{s_row.document_id}]")



@Singleton
class StaffDatabase(DataHelper):
    def __init__(self):
        self.staff = DatabaseConnect(application='staff', dictionary=True)
        self.master_list_table: Table = self.automation.db.table(table_name='master_list', dictionary=True)


    def get_staff_member(self, user_name) -> Result:
        first_name = ''
        last_name = ''
        parts = user_name.split(' ')
        if len(parts) == 2 :
            first_name = parts[0]
            last_name = parts[1]
        return self.master_list_table.fetch_many(where=f"`first_name` = '{first_name}' and `last_name` = '{last_name}'")