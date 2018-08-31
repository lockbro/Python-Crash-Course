"""
7-2

1.编写一个程序，询问有多少用户就餐·
2.超过8人就说明没有空桌，否则就打印说明有空桌
"""

people = input("How many peole would come to have a dinner?")
if int(people) > 8 :
    print("We dont have that much table.")
else:
    print("We have surplus table.")
