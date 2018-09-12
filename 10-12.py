"""
10-12 记住喜欢的数字 ：

将练习 10-11 中的两个程序合而为一。
如果存储了用户喜欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。
运行这个程序两次，看看它是否像预期的那样工作。
"""


import json

try:
    with open("favoritenumber.txt") as handle_file:
        number = json.load(handle_file)
        print("I know your favorite number! It's " + number + '.')
except FileNotFoundError:
    favoriteNumber = input("What's your favorite number : ")
    with open("favoritenumber.txt", 'w') as handle_file:
        json.dump(favoriteNumber, handle_file)
