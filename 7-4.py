"""
7-4

1.输入一个循环，提示用户输入一系列的比萨配料，并在输入quit的时候结束循环
2.每输入一种配料就打印一条消息显示已经添加了配料

"""

client_want = "_"
while client_want != "quit":
    client_want = input("input what you want to add : ")
    if client_want == "quit":
        print("Ok,please wait a second.")
    else:
        print("you have add " + client_want)
