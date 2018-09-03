"""
8-11 不变的魔术师 ：

修改你为完成练习 8-10 而编写的程序，
在调用函数 make_great() 时，向它传递魔术师列表的副本。
由于不想修改原始列表，请返回修改后的列表，并将其存储到另一个列表中。
分别使用这两个列表来调用 show_magicians() ，
确认一个列表包含的是原来的魔术师名字，而另一个列表包含的是添加了字
样 “the Great” 的魔术师名字
"""

magician_name = ["Xiao", "Jay", "Mike"]
blank_list = []


def make_great(origin_list, blank):
    for name in origin_list:
        greatMagician = "the Great " + name
        blank.append(greatMagician)
    return blank


def show_magicians(list):
    for name in list:
        print(name)


show_magicians(magician_name)
blank_list = make_great(magician_name, blank_list)
show_magicians(blank_list)
show_magicians(magician_name)
