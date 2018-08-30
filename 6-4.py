"""6-4

1.选5个编程词汇作为字典里面的键，并将含义作为值存在词汇表中。
2.打印出每个词汇以及它的含义。
3.用循环的的方式遍历输出
4.再添加另外五个词语以及他们的功能（略）

"""
Python_words = {
	"print" : "打印",
	"for" : "循环关键字",
	"list" : "转换为列表的方法",
	"range" : "表示范围",
	"reverse" : "可以将列表进行反转的方法"
}

for name, func in Python_words.items():
	print(name + ":\n\t" + func + "." )