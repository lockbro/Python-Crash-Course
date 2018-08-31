"""6-3
Python字典可用于模拟生活中的字典，在Python中为了不混淆，我们把它称为词汇表

1.选5个编程词汇作为字典里面的键，并将含义作为值存在词汇表中。
2.打印出每个词汇以及它的含义。

"""
Python_words = {
	"print" : "打印",
	"for" : "循环关键字",
	"list" : "转换为列表的方法",
	"range" : "表示范围",
	"reverse" : "可以将列表进行反转的方法"
}

print("print:\n" + "    " + Python_words["print"])
print("for:\n" + "    " + Python_words["for"])
print("list:\n" + "    " + Python_words["list"])
print("range:\n" + "    " + Python_words["range"])
print("reverse:\n" + "    " + Python_words["reverse"])
