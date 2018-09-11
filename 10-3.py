"""
10-3 访客 ：

编写一个程序，提示用户输入其名字；
用户作出响应后，将其名字写入到文件 guest.txt 中。
"""


while True:
    user_name = input("What's your name : ")
    if user_name == 'quit':
        break
    else:
        with open("guest.txt", "a+") as handle_file:
            handle_file.write(user_name + '\n')
        handle_file.close()
