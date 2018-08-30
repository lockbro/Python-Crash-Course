""""
6-6

1.创建一个应该会接受调查的人员名单，其中有的人已经在字典中，有的没有
2.遍历这个人员名单，对于已经参加过的人打印一条表示感谢，对于未参加过调查的人打印一条消息邀请他参加调查。
"""

favorite_language = {
	"jem" : "python",
	"sarah" : "c",
	"edward" : "ruby",
	"phil" : "python",
}

should_be_investigate = ["jay" , "tom" , "phil" , "lemon","sarah"]

for person in should_be_investigate:
	if person in favorite_language.keys():
		print("Thank you for participating our survey," + person)
	else:
		print("Hello " + person + ",we invite you to participate our survey!")
