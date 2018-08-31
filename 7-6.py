"""
7-5

有个电影院按年龄不同收取不同费用
1.编写一个循环，询问用户的年龄：
（1）不到3岁的观众免费
（2）3-12岁的观众需要收$10
（3）超过12岁的观众需要收$15
按照年龄来收取价钱

2.在while循环中使用条件测试来结束循环
3.使用变量active来控制循环的时机
4.使用break语句在用户输入"quit"的时候退出循环

"""

active = True
while active:
    client_age = input("What's the client's age : ")
    if client_age == "quit":
        active = False
    elif int(client_age) < 3:
        print("We won't charge for the guy.")
    elif int(client_age) < 12:
        print("We will charge 10 dollar.")
    elif int(client_age) >= 12:
        print("We will charge 15 dollar.")
