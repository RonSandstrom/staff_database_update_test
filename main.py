# This is a sample Python script.
from threestep.result.c_result import Result
from threestep.std_logging.logs import init_logs, logger

from database_tables.automation_database import AutomationDatabaseTables
from database_tables.c_staff_master_list_table import StaffMasterList


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main() -> Result:
    db: AutomationDatabaseTables = AutomationDatabaseTables.Instance()

    p_result = db.get_not_process_staff()
    show_result(p_result)

    ach_result = db.get_ach_error_items()
    show_result(ach_result)

    w9_result = db.get_w9_error_items()
    show_result(w9_result)

    return Result(0)


if __name__ == '__main__':
    tracker = init_logs('staff_database_update_test', console=True, the_version='2.0.0', log_to_file=False,
                        log_level='info', project_name='webhooks', vm_name='App Engine', job_type='WebHook')
    tracker.start()

    result = main()

    tracker.end(result.message)

