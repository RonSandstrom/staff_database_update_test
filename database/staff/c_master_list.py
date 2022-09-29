from threestep.std_utility.c_datetime import DateTime
from threestep.database.v2_c_database_operations import DatabaseOperations


class MasterList(DatabaseOperations):
    def __init__(self, row=None, t_tuple=None):
        super().__init__(_schema, _table, _field_map)
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
            
        
_schema = 'staff'
_table = 'master_list'
_field_map = {            
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

