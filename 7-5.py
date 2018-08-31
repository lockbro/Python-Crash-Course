"""
7-5

有个电影院按年龄不同收取不同费用
1.编写一个循环，询问用户的年龄：
（1）不到3岁的观众免费
（2）3-12岁的观众需要收$10
（3）超过12岁的观众需要收$15
按照年龄来收取价钱
"""

client_age = "_"
while client_age != "quit":
    client_age = input("What's the client's age : ")
    if client_age == "quit":
        break;
    elif int(client_age) < 3:
        print("We won't charge for the guy.")
    elif int(client_age) < 12:
        print("We will charge 10 dollar.")
    elif int(client_age) >= 12:
        print("We will charge 15 dollar.")
