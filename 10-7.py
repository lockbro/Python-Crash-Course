"""
10-7 加法计算器 ：

将你为完成练习 10-6 而编写的代码放在一个 while 循环中，
让用户犯错（输入的是文本而不是数字）后能够继续输入数字
"""


while True:
    two_number = input("Please input two number (split with space): ")
    if two_number != "quit":
        numbers = two_number.split(" ")
        try:
            reslut = int(numbers[0]) + int(numbers[1])
        except ValueError:
            print("Sorry ,only both number is integer can they add.")
        else:
            print(reslut)
    else:
        break
