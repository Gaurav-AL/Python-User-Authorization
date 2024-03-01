'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

from collections import defaultdict

class User:
    def __init__(self, user_id, user_name,user_age,user_hobby):
        self.user_id = user_id
        self.user_name = user_name
        self.user_age = user_age
        self.user_hobby = user_hobby
    
    def __str__(self):
        return f"user-id : {self.user_id}, user-name : {self.user_name}, user-age :{self.user_age},user-hobby : {self.user_hobby}"
list_users = defaultdict(User)
def fetch_profile(user_id):
    profile = view_profile(user_id)
    
    if(profile):
        print(profile)
    else:
        print("User Doesn't Exist's :(")

def view_profile(user_id):
    if user_id in list_users:
        return list_users[user_id]
    return None

def register_user():
    user_id = input("Enter user id :")
    user_name = input("Enter user name :")
    user_age = input("Enter user age :")
    user_hobby = input("Enter user personal favourite hobby :")
    list_users[user_id] = User(user_id,user_name,user_age,user_hobby)
    
no_of_users = input("Enter Number of users you want to register :")
for i in range(int(no_of_users)):
    print(f"Enter {i+1} Details")
    register_user()
user_id = input("Enter User id to view profile :")
fetch_profile(user_id)
