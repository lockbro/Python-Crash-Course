"""
10-11 喜欢的数字 ：

编写一个程序，提示用户输入他喜欢的数字，并使用 json.dump() 将这个数字存储到文件中。
再编写一个程序，从文件中读取这个值，
并打印消息 “I know your favorite number! It's _____.” 。
"""


import json

favoriteNumber = input("What's your favorite number : ")
with open("favoritenumber.txt", 'w') as handle_file:
    json.dump(favoriteNumber, handle_file)

with open("favoritenumber.txt") as handle_file:
    number = json.load(handle_file)
    print("I know your favorite number! It's " + number + '.')
