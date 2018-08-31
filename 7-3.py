"""
7-3

1.让用户输入一个数字，并指出是否为10的整数倍
"""

num = input("Please input a number : ")
if int(num) % 10 == 0 :
    print(num + " integer is 10")
else:
    print(num + " integer is not 10")
