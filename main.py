# This is a sample Python script.
from threestep.result.c_result import Result
from threestep.std_logging.logs import init_logs, logger
from database.automation.automation_database import AutomationDatabase
from database.automation.c_sign_now_documents_table import SignNowDocument
from database.staff.c_staff_master_list_table import StaffMasterList
from database.staff.staff_database import StaffDatabase


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def show_staff_user(user_name: str):
    db: StaffDatabase = StaffDatabase.Instance()

    staff_result = db.get_staff_member(user_name)
    if staff_result.is_ok():
        for row in staff_result.data:
            member: StaffMasterList = StaffMasterList(row=row)
            logger.info(f"Found {member.first_name}, {member.last_name}")

def show_signnow_documents() -> Result:
    db: AutomationDatabase = AutomationDatabase.Instance()

    p_result = db.get_not_process_staff()
    db.show_result('process_staff', p_result)

    ach_result = db.get_company_ach_documents()
    db.show_result('ach', ach_result)

    w9_result = db.get_staff_ach_documents()
    db.show_result('w9', w9_result)

    return Result(0)


if __name__ == '__main__':
    tracker = init_logs('staff_database_update_test', console=True, the_version='2.0.0', log_to_file=False,
                        log_level='info', project_name='webhooks', vm_name='App Engine', job_type='WebHook')
    tracker.start()

    result = show_signnow_documents()

    tracker.end(result.message)

