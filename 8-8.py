"""
8-8 用户的专辑 ：
在为完成练习 8-7 编写的程序中，编写一个 while 循环，让用户输入一个专辑的歌手和名称。

获取这些信息后，使用它们来调用函数 make_album() ，并将创建的字典打印出来。
在这个 while 循环中，务必要提供退出途径。
"""


def make_album(singerName, albumName):
    album_dict = {"singer": singerName, "album": albumName}
    return album_dict


while True:
    singer = input("What's the name of the singer : ")
    if singer == "q":
        break
    album = input("What's your favourite album of the " + singer + ": ")
    if album == "q":
        break
    finish_album = make_album(singer, album)
    print(finish_album)
