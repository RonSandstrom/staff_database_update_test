from threestep.std_utility.c_datetime import DateTime
from threestep.database.v2_c_database_operations import DatabaseOperations


class SignnowSignedDocuments(DatabaseOperations):
    def __init__(self, row=None, t_tuple=None):
        super().__init__(_schema, _table, _field_map)
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
            
        
_schema = 'automation'
_table = 'signnow_signed_documents'
_field_map = {            
        'document_id': 'document_id', 'access_token': 'access_token', 'user_name': 'user_name', 
        'user_id': 'user_id', 'document_name': 'document_name', 'document': 'document', 
        'processed': 'processed', 'signed_date_time': 'signed_date_time', 'processed_date_time': 'processed_date_time', 
        'processed_staff_database': 'processed_staff_database', 'processed_staff_database_date': 'processed_staff_database_date', }

