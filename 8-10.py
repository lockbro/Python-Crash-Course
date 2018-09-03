"""
8-10 了不起的魔术师 ：

在你为完成练习 8-9 而编写的程序中，
编写一个名为 make_great() 的函数，对魔术师列表进行修改，在每个魔术师的名字中都加入字样 “the
Great” 。
调用函数 show_magicians() ，确认魔术师列表确实变了。
"""

magician_name = ["Xiao", "Jay", "Mike"]


def make_great(list):
    for index, name in enumerate(list):
        list[index] = "the Great " + name


def show_magicians(list):
    for name in list:
        print(name)


make_great(magician_name)
show_magicians(magician_name)
