"""
10-9 沉默的猫和狗 ：

修改你在练习 10-8 中编写的 except 代码块，让程序在文件不存在时一言不发
"""


def read_file(filename):
    with open(filename) as handle_file:
        contents = handle_file.read()
        print(contents)


file_list = ["cats.txt", "dogs.txt"]

for file in file_list:
    try:
        read_file(file)
    except FileNotFoundError:
        pass
