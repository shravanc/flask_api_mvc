from app import mongo

class User():

    @classmethod
    def get(self):
        users = mongo.db.users.find()
        user_list = []
        for user in users:
            data = {}
            data['first_name'] = user['first_name']
            data['last_name'] =  user['last_name']
            user_list.append(data)
        return user_list

