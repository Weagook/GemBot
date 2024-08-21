class FakeDatabase:
    def __init__(self):
        self.TEMP_DATABASE = {}
    
    def add_user_by_id(self, id):
        self.TEMP_DATABASE[id] = {}

    def add_user_name(self, id, name):
        self.TEMP_DATABASE[id]['name'] = name


DATABASE = FakeDatabase()