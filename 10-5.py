"""
10-5 关于编程的调查 ：

编写一个 while 循环，询问用户为何喜欢编程。
每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。
"""


common_sentence = ' just visited and the reason\
why he(her)love to code is that '

while True:
    user_name = input("What's your name : ")
    if user_name != 'quit' and len(user_name) != 0:
        print("Hello " + user_name + ".")
        reason = input("why you love to code : ")
        with open("guest_book.txt", "a+") as handle_file:
            handle_file.write(user_name + common_sentence + reason + '\n')
        handle_file.close()
    else:
        break
