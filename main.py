# This is a sample Python script.
from threestep.result.c_result import Result
from threestep.std_logging.logs import init_logs, logger
from database.automation.automation_database import AutomationDatabase
from database.automation.c_sign_now_document import SignNowDocument
from database.c_database_connections import DBC

from database.staff.c_master_list import MasterList
from database.staff.staff_database import StaffDatabase


def get_staff_member(user_name) -> Result:
    dc: DBC = DBC.Instance()
    staff = dc.table(application='staff', table='master_list')

    first_name = ''
    last_name = ''
    parts = user_name.split(' ')
    if len(parts) == 2:
        first_name = parts[0]
        last_name = parts[1]
    return staff.fetch_many(where=f"`first_name` = '{first_name}' and `last_name` = '{last_name}'")

def show_result(class_type, label: str, result: Result = Result(-1)):
    if result.is_ok():
        for row in result.data:
            s_row = class_type(row=row)
            logger.info(f"[{label}] Located record for [{s_row.user_name}] doc id = [{s_row.document_id}]")


def get_not_process_staff() -> Result:
    dc: DBC = DBC.Instance()
    table = dc.table(application='automation', table='signnow_signed_documents')
    return table.fetch_many(
        where="`processed_staff_database` = 'N'")

def get_staff_ach_documents() -> Result:
    dc: DBC = DBC.Instance()
    table = dc.table(application='automation', table='signnow_signed_documents')
    return table.fetch_many(
        where="`document_name` like 'Sub W9%' and `user_name` != 'ERROR' and `processed` = 'N'")


def get_company_ach_documents() -> Result:
    dc: DBC = DBC.Instance()
    table = dc.table(application='automation', table='signnow_signed_documents')
    return table.fetch_many(
        where="document_name ='Company SUB W-9_ACH' and `user_name` != 'ERROR' and `processed` = 'N'")


def update_processed_staff(id, processed_date_time):
    dc: DBC = DBC.Instance()
    table = dc.table(application='automation', table='signnow_signed_documents')
    update_set = {
        'processed_staff_database': 'Y',
        'processed_staff_database_date': f'{processed_date_time}'
    }
    return table.update(_the_dict=update_set, where=f"document_id = '{id}'")


def update_staff_user_name(id, document_user_name):
    dc: DBC = DBC.Instance()
    table = dc.table(application='automation', table='signnow_signed_documents')
    update_set = {
        'user_name': f'{document_user_name}',
    }
    return table.update(_the_dict=update_set, where=f"document_id = '{id}'")


def show_staff_user(user_name: str):
    staff_result = get_staff_member(user_name)
    if staff_result.is_ok():
        for row in staff_result.data:
            member: MasterList = MasterList(row=row)
            logger.info(f"Found {member.first_name}, {member.last_name}")


def show_signnow_documents() -> Result:
    dc: DBC = DBC.Instance().table(application='automation', table='signnow_signed_documents')

    a_result = dc.fetch_many(limit="10")
    show_result(SignNowDocument, 'allf', a_result)

    p_result = get_not_process_staff(documents_table)
    show_result(SignNowDocument, 'process_staff', p_result)

    ach_result = get_company_ach_documents(documents_table)
    show_result(SignNowDocument, 'ach', ach_result)

    w9_result = get_staff_ach_documents(documents_table)
    show_result(SignNowDocument, 'w9', w9_result)

    return Result(0)


if __name__ == '__main__':
    tracker = init_logs('staff_database_update_test', console=True, the_version='2.0.0', log_to_file=False,
                        log_level='info', project_name='webhooks', vm_name='App Engine', job_type='WebHook')
    tracker.start()

    result = show_signnow_documents()

    tracker.end(result.message)
