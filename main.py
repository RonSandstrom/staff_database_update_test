
from threestep.database.c_database_connections import DBC
from threestep.database.c_table import Table
from threestep.result.c_result import Result
from threestep.std_logging.logs import init_logs, logger

from c_master_list import MasterList
from c_signnow_signed_documents import SignnowSignedDocuments

sd_table: Table = DBC.Instance().table(application='automation', table='signnow_signed_documents')
staff_table: Table = DBC.Instance().table(application='staff_db', table='master_list')


def get_staff_member(user_name) -> Result:
    first_name = ''
    last_name = ''
    parts = user_name.split(' ')
    if len(parts) == 2:
        first_name = parts[0]
        last_name = parts[1]
    return staff_table.fetch_many(where=f"`first_name` = '{first_name}' and `last_name` = '{last_name}'")


def show_result(class_type, label: str, result: Result = Result(-1)):
    if result.is_ok():
        for row in result.data:
            s_row = class_type(row=row)
            logger.info(f"[{label}] Located record for [{s_row.user_name}] doc id = [{s_row.document_id}]")


def get_not_process_staff() -> Result:
    return sd_table.fetch_many(
        where="`processed_staff_database` = 'N'")


def get_staff_ach_documents() -> Result:
    return sd_table.fetch_many(
        where="`document_name` like 'Sub W9%' and `user_name` != 'ERROR' and `processed` = 'N'")


def get_company_ach_documents() -> Result:
    return sd_table.fetch_many(
        where="document_name ='Company SUB W-9_ACH' and `user_name` != 'ERROR' and `processed` = 'N'")


def update_processed_staff(id, processed_date_time):
    update_set = {
        'processed_staff_database': 'Y',
        'processed_staff_database_date': f'{processed_date_time}'
    }
    return sd_table.update(_the_dict=update_set, where=f"document_id = '{id}'")


def update_staff_user_name(id, document_user_name):
    update_set = {
        'user_name': f'{document_user_name}',
    }
    return sd_table.update(_the_dict=update_set, where=f"document_id = '{id}'")


def show_staff_user(user_name: str):
    staff_result = get_staff_member(user_name)
    if staff_result.is_ok():
        for row in staff_result.data:
            member: MasterList = MasterList(row=row)
            logger.info(f"Found {member.first_name}, {member.last_name}")


def show_signnow_documents() -> Result:

    a_result = sd_table.fetch_many(limit="10")
    show_result(SignnowSignedDocuments, 'allf', a_result)

    p_result = get_not_process_staff()
    show_result(SignnowSignedDocuments, 'process_staff', p_result)

    ach_result = get_company_ach_documents()
    show_result(SignnowSignedDocuments, 'ach', ach_result)

    w9_result = get_staff_ach_documents()
    show_result(SignnowSignedDocuments, 'w9', w9_result)

    return Result(0)


if __name__ == '__main__':
    tracker = init_logs('staff_database_update_test', console=True, the_version='2.0.0', log_to_file=False,
                        log_level='info', project_name='webhooks', vm_name='App Engine', job_type='WebHook')
    tracker.start()

    result = show_signnow_documents()

    tracker.end(result.message)
