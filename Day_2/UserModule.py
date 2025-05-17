# module is .py file
# This module contains the User functions, class and its methods and variable

user_info= {}     # global declaration

def get_all_user_info():
    return user_info

def add_user_info(user_id, user_name, user_email):
    user_info[user_id] = { 'user_name': user_name,
                            'user_email': user_email}
                          