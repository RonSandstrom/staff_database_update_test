from threestep.database.c_database_connect import DatabaseConnect
from threestep.database.c_table import Table
from threestep.cache.c_singleton import Singleton
from threestep.result.c_result import Result
from threestep.std_utility.c_utility import Utility
import re
from threading import Lock


@Singleton
class DatabaseTables(object):
    lock = Lock()

    def __init__(self):
        self.staff = DatabaseConnect(application='localhost_staff', dictionary=True)
        self.staff_table: Table = self.staff.db.table(table_name='master_list', dictionary=True)




    def is_empty(self, x):
        if x is None or len(str(x)) == 0:
            return True
        return False

    def titlecase(self, s):
        return re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda word: word.group(0).capitalize(), s)

    def get_sports(self) -> []:
        self.sports = []
        query = f"select distinct `sport` from `netsuite`.`monday_class_id_table`"
        result = self.netsuite_class_list_table.fetch(query)
        if result.is_ok():
            self.sports.append("Select a Sport")
            for row in result.data:
                sport = row.get('sport', '')
                sport = self.titlecase(sport)
                sport = Utility.trim_all_extra_white_space(sport)
                self.sports.append(sport)
        return self.sports

    def get_classes(self, sport: str = None, text: str = None):
        self.lock.acquire()
        retval = []
        sport_part = ''
        and_part = ''
        text_part = ''
        base_and = ''
        if sport:
            sport_part = f"`sport` = '{sport}'"
        if sport and text:
            and_part = ' AND '
        if text:
            s = text.split(' ')
            if isinstance(s, str):
                text_part = f"`name` like '%{text}%'"
            elif isinstance(s, list):
                first = True
                for word in s:
                    if first:
                        text_part = f"`name` like '%{word}%'"
                        first = False
                    else:
                        text_part += f" AND `name` like '%{word}%'"


        if sport or text:
            base_and = ' AND '

        query = f"where `name` like '%:%' and length(`name`) > 0 {base_and} {sport_part}{and_part}{text_part}"

        result = self.netsuite_class_list_table.fetch_many(where=query)

        if result.is_ok():
            for row in result.data:
                data = row.get('name')
                if len(data.strip()) > 0:
                    retval.append(data)

        self.lock.release()
        return retval




