"""
10-13 验证用户 ：

最后一个 remember_me.py 版本假设用户要么已输入其用户名，要么是首次运行该程序。
我们应修改这个程序，以应对这样的情形：
当前和最后一次运行该程序的用户并非同一个人。
为此，在 greet_user() 中打印欢迎用户回来的消息前，先询问他用户名是否是对的。
如果不对，就调用 get_new_username() 让用户输入正确的用户名。
"""


import json


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """ 提示用户输入用户名 """
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username


def greet_user():
    """ 问候用户，并指出其名字 """
    username = get_stored_username()
    if username:
        Answer = input("Is the name " + username + " right?(y/n) : ")
        if Answer == 'y':
            print("Welcome back, " + username + "!")
        elif Answer == 'n':
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
