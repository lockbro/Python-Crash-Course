"""6-2
用一个字典存5个人的名字以及他们喜欢的数字，最后打印成一句话。
"""
favorite_color = {
	"Tom" : 5,
	"Jay" : 34,
	"Mike" : 13,
	"Halen" : 54,
	"Paul" : 40,
}

for person, number in favorite_color.items():
	print(person + "'s favorite color is " + str(number))


