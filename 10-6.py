"""
10-6 加法运算 ：

提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数字。
在这种情况下，当你尝试将输入转换为整数时，将引发 TypeError 异常。
编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。
在用户输入的任何一个值不是数字时都捕获 TypeError 异常，并打印一条友好的错误消息。
对你编写的程序进行测试：先输入两个数字，再输入一些文本而不是数字。
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
