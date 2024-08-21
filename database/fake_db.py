from ..config import TEMP_DATABASE

class FakeDatabase:
    def __init__(self):
        self.TEMP_DATABASE = TEMP_DATABASE
    
    def add_user_by_id(self, id):
        self.TEMP_DATABASE[id] = {}


DATABASE = FakeDatabase()