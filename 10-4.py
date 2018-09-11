"""
10-4 访客名单 ：

编写一个 while 循环，提示用户输入其名字。
用户输入其名字后，在屏幕上打印一句问候语，并将一条访问记录添加到文件 guest_book.txt 中。
确保这个文件中的每条记录都独占一行。
"""


while True:
    user_name = input("What's your name : ")
    if user_name != 'quit' and len(user_name) != 0:
        print("Hello " + user_name + ".")
        with open("guest_book.txt", "a+") as handle_file:
            handle_file.write(user_name + ' just visited\n')
        handle_file.close()
    else:
        break
