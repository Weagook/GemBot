from utils import referal_link

class FakeDatabase:
    def __init__(self):
        self.TEMP_DATABASE = {}
    
    def add_user_by_id(self, user_id):
        self.TEMP_DATABASE[user_id] = {}
        self.TEMP_DATABASE[user_id]['status'] = 'Player'
        self.TEMP_DATABASE[user_id]['spins'] = 30
        self.TEMP_DATABASE[user_id]['followers'] = []
        self.TEMP_DATABASE[user_id]['link'] = referal_link(user_id)
        self.TEMP_DATABASE[user_id]['points'] = 0

    def add_user_name(self, user_id, name):
        self.TEMP_DATABASE[user_id]['name'] = name

    def add_follower(self, user_id, follower_id):
        if not (follower_id in self.TEMP_DATABASE[user_id]['followers']):
            self.TEMP_DATABASE[user_id]['followers'].append(follower_id)
    
    def count_followers(self, user_id) -> int:
        return len(self.TEMP_DATABASE[user_id]['followers'])

    def get_followers(self, user_id) -> list:
        return self.TEMP_DATABASE[user_id]['followers']
    
    def is_exists(self, user_id):
        if self.TEMP_DATABASE.get(user_id, False):
            return True
        return False

    def get_link(self, user_id):
        return self.TEMP_DATABASE[user_id]['link']
    
    def get_spins(self, user_id):
        return self.TEMP_DATABASE[user_id]['spins']

    def remove_spin(self, user_id):
        self.TEMP_DATABASE[user_id]['spins'] -= 1

    def get_points(self, user_id):
        return self.TEMP_DATABASE[user_id]['points']

    def add_points(self, user_id, points):
        self.TEMP_DATABASE[user_id]['points'] += points
    
    def get_all_users(self):
        return self.TEMP_DATABASE

DATABASE = FakeDatabase()