from threestep.database.c_database_connect import DatabaseConnect
from threestep.database.c_table import Table
from threestep.cache.c_singleton import Singleton
from threestep.result.c_result import Result
from threestep.std_logging.logs import logger
from database.automation.c_sign_now_documents_table import SignNowDocument


@Singleton
class AutomationDatabase(object):

    def __init__(self):
        self.automation = DatabaseConnect(application='automation', dictionary=True)
        self.documents_table: Table = self.automation.db.table(table_name='signnow_signed_documents', dictionary=True)

    def show_result(self, label: str, result: Result = Result(-1)):
        if result.is_ok():
            for row in result.data:
                s_row: SignNowDocument = SignNowDocument(row=row)
                logger.info(f"[{label}] Located record for [{s_row.user_name}] doc id = [{s_row.document_id}]")

    def get_not_process_staff(self) -> Result:
        return self.documents_table.fetch_many(
            where="`processed_staff_database` = 'N'")

    def get_staff_ach_documents(self) -> Result:
        return self.documents_table.fetch_many(
            where="`document_name` like 'Sub W9%' and `user_name` != 'ERROR' and `processed` = 'N'")

    def get_company_ach_documents(self) -> Result:
        return self.documents_table.fetch_many(
            where="document_name ='Company SUB W-9_ACH' and `user_name` != 'ERROR' and `processed` = 'N'")

    def update_processed_staff(self, id, processed_date_time):
        update_set = {
            'processed_staff_database': 'Y',
            'processed_staff_database_date': f'{processed_date_time}'
        }
        return self.documents_table.update(_the_dict=update_set, where =f"document_id = '{id}'")

    def update_staff_user_name(self, id, document_user_name):
        update_set = {
            'user_name': f'{document_user_name}',
        }
        return self.documents_table.update(_the_dict=update_set, where=f"document_id = '{id}'")

"""
document_query = "SELECT document, document_name, document_id, signed_date_time FROM automation.signnow_signed_documents WHERE processed_staff_database='N'"
 
document_query = "SELECT document, document_id, signed_date_time FROM automation.signnow_signed_documents where document_name like 'Sub W9%' and user_name != 'ERROR' and processed='N'"
 
document_query = "SELECT document, document_id, signed_date_time FROM automation.signnow_signed_documents where document_name ='Company SUB W-9_ACH
' and user_name != 'ERROR' and processed='N'"
 
 
Also the following updates
 
update_query = "UPDATE `automation`.`signnow_signed_documents` SET processed_staff_database='Y', processed_staff_database_date='" + processed_date_time + "' WHERE document_id=\"" + id + "\""
 
update_query = "UPDATE `automation`.`signnow_signed_documents` SET user_name=\"" + document_user_name + "\" WHERE document_id=\"" + id + "\""
 
update_query = "UPDATE `automation`.`signnow_signed_documents` SET user_name=\"" + document_user_name + "\" WHERE document_id=\"" + id + "\""
 
"""



