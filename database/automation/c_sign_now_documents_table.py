from threestep.std_utility.c_datetime import DateTime


class SignNowDocument:
    class_map = {            
        'document_id': 'document_id', 'access_token': 'access_token', 'user_name': 'user_name', 
        'user_id': 'user_id', 'document_name': 'document_name', 'document': 'document', 
        'processed': 'processed', 'signed_date_time': 'signed_date_time', 'processed_date_time': 'processed_date_time', 
        'processed_staff_database': 'processed_staff_database', 'processed_staff_database_date': 'processed_staff_database_date', }

    def __init__(self, row=None, t_tuple=None):
        self.document_id = None
        self.access_token = None
        self.user_name = None
        self.user_id = None
        self.document_name = None
        self.document = None
        self.processed = None
        self.signed_date_time = None
        self.processed_date_time = None
        self.processed_staff_database = None
        self.processed_staff_database_date = None

        if row is not None:
            self.load_from_dict(row)
      
        if t_tuple is not None:
            self.load_from_tuple(t_tuple)
    
    def load_from_tuple(self, t_tuple):
        pos = 0
        key = list(vars(self).keys())
        for v in t_tuple:
            setattr(self, key[pos], v)
            pos += 1
            
    def load_from_dict(self, t_row):
        for k, v in t_row.items():
            if k in self.class_map:
                setattr(self, self.class_map.get(k), v)

    @staticmethod
    def row_get(row, name, default=None, c_type=None):
        if row is None:
            return default
        x = row.get(name, default)
        if x is None:
            x = default
        return x
    
    @staticmethod
    def f_schema(name):
        if name is None:
            return ''
        return f'`{name}`.'
        
    def gen_parm_list(self):
        return ', '.join('%s'.format(k) for k, v in self.class_map.items())

    def gen_update_values(self):
        return ', '.join('`{0}` = values(`{0}`)'.format(k) for k, v in self.class_map.items())

    def as_dict(self):
        return vars(self)
            
    def as_db_fields(self):
        return ', '.join('`{0}`'.format(k) for k, v in self.class_map.items())

    def as_db_values(self):
        return tuple(vars(self).values())
        
    def as_tuple(self):
        return tuple(vars(self).values())
        
    def insert_query(self, schema=None):
        return f"INSERT INTO {self.f_schema(schema)}`signnow_signed_documents` ({self.as_db_fields()}) VALUES ({self.gen_parm_list()})"

    def replace_query(self, schema=None):
        return f"REPLACE INTO {self.f_schema(schema)}`signnow_signed_documents` ({self.as_db_fields()}) VALUES ({self.gen_parm_list()})"

    def insert_on_duplicate_update_query(self, schema=None):
        return f"INSERT INTO {self.f_schema(schema)}`signnow_signed_documents` ({self.as_db_fields()}) VALUES ({self.gen_parm_list()}) ON DUPLICATE KEY UPDATE {self.gen_update_values()}"

    @staticmethod
    def delete_query(schema: str, key: str, data: any):
        return f"delete from {SignNowDocument.f_schema(schema)}`signnow_signed_documents` where `{key}` = '{data}'"
