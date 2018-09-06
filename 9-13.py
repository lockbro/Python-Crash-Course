"""
9-13 使用 OrderedDict ：

在练习 6-4 中，你使用了一个标准字典来表示词汇表。
--------------------------------------------------------
Python_words = {
    "print": "打印",
    "for": "循环关键字",
    "list": "转换为列表的方法",
    "range": "表示范围",
    "reverse": "可以将列表进行反转的方法"
}
--------------------------------------------------------
请使用 OrderedDict 类来重写这个程序，并确认输出的顺序与你在字典中添加
键— 值对的顺序一致。
"""
from collections import OrderedDict

python_words = OrderedDict()

python_words["print"] = "打印"
python_words["for"] = "循环关键字"
python_words["list"] = "转换为列表的方法"
python_words["range"] = "表示范围"
python_words["reverse"] = "可以将列表进行反转的方法"

for key, value in python_words.items():
    print(key + ":\n\t" + value + ".")
