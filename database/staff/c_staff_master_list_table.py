from threestep.std_utility.c_datetime import DateTime


class StaffMasterList:
    class_map = {            
        'dbkey': 'dbkey', 'sid': 'sid', 'first_name': 'first_name', 
        'last_name': 'last_name', 'email': 'email', 'phone_number': 'phone_number', 
        'zip_code': 'zip_code', 'city': 'city', 'state': 'state', 
        'address': 'address', 'vendor_id': 'vendor_id', 'sport': 'sport', 
        'company': 'company', 'role': 'role', 'group': 'group', 
        'work_status': 'work_status', 'w9_received': 'w9_received', 'ach_received': 'ach_received', 
        'w9_signed_date_time': 'w9_signed_date_time', 'background_check_status': 'background_check_status', 'background_check_expire': 'background_check_expire', 
        'abuse_training': 'abuse_training', 'abuse_training_expire': 'abuse_training_expire', 'google_check': 'google_check', 
        'usa_membership': 'usa_membership', 'ica_signed_date_time': 'ica_signed_date_time', 'notes': 'notes', 
        'created': 'created', 'updated': 'updated', 'update_by_user': 'update_by_user', 
        'netsuite_vendor_id': 'netsuite_vendor_id', 'csv_filename': 'csv_filename', 'concussion_training': 'concussion_training', }

    def __init__(self, row=None, t_tuple=None):
        self.dbkey = None
        self.sid = None
        self.first_name = None
        self.last_name = None
        self.email = None
        self.phone_number = None
        self.zip_code = None
        self.city = None
        self.state = None
        self.address = None
        self.vendor_id = None
        self.sport = None
        self.company = None
        self.role = None
        self.group = None
        self.work_status = None
        self.w9_received = None
        self.ach_received = None
        self.w9_signed_date_time = None
        self.background_check_status = None
        self.background_check_expire = None
        self.abuse_training = None
        self.abuse_training_expire = None
        self.google_check = None
        self.usa_membership = None
        self.ica_signed_date_time = None
        self.notes = None
        self.created = None
        self.updated = None
        self.update_by_user = None
        self.netsuite_vendor_id = None
        self.csv_filename = None
        self.concussion_training = None

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
        return f"INSERT INTO {self.f_schema(schema)}`master_list` ({self.as_db_fields()}) VALUES ({self.gen_parm_list()})"

    def replace_query(self, schema=None):
        return f"REPLACE INTO {self.f_schema(schema)}`master_list` ({self.as_db_fields()}) VALUES ({self.gen_parm_list()})"

    def insert_on_duplicate_update_query(self, schema=None):
        return f"INSERT INTO {self.f_schema(schema)}`master_list` ({self.as_db_fields()}) VALUES ({self.gen_parm_list()}) ON DUPLICATE KEY UPDATE {self.gen_update_values()}"

    @staticmethod
    def delete_query(schema: str, key: str, data: any):
        return f"delete from {StaffMasterList.f_schema(schema)}`master_list` where `{key}` = '{data}'"
