'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

from collections import defaultdict
import random
class User:
    def __init__(self, user_id, user_name,user_age,user_hobby,user_privilege_level):
        self.user_id = user_id
        self.user_name = user_name
        self.user_age = user_age
        self.user_hobby = user_hobby
        self.user_privilege_level = user_privilege_level
    
    def __str__(self):
        return f"user-id : {self.user_id}, user-name : {self.user_name}, user-age :{self.user_age},user-hobby : {self.user_hobby}"
list_users = defaultdict(User)
def fetch_profile(user_id,requesting_user):
    profile = view_profile(user_id,requesting_user)
    
    if(profile):
        print(profile)
    else:
        print("User Doesn't Exist's :(")

def view_profile(user_id, requesting_user):
    if user_id in list_users and requesting_user in list_users:
        if(list_users[requesting_user].user_privilege_level >= 2):#checking user access privilege.
            return list_users[user_id]
        else:
            return "Insufficient Privileges!!"
    return None

def register_user():
    user_id = input("Enter user id :")
    user_name = input("Enter user name :")
    user_age = input("Enter user age :")
    user_hobby = input("Enter user personal favourite hobby :")
    if(int(user_age) <= 23):
        user_privilege_level = random.randint(3,10)
    else:
        user_privilege_level = random.randint(0,3)
    list_users[user_id] = User(user_id,user_name,user_age,user_hobby,user_privilege_level)
    
no_of_users = input("Enter Number of users you want to register :")
for i in range(int(no_of_users)):
    print(f"Enter {i+1} Details")
    register_user()
user_id = input("Enter User id to view profile :")
requesting_user = input("Login to your Account \n\tEnter your id :")
fetch_profile(user_id,requesting_user)
