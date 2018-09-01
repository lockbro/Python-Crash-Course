"""6-7

1.创建一个people列表，字典中用字典存三个人的信息
2.遍历这个列表，将每个人的所有信息都打印出来
"""

LockBro = {
		"First_name":"Lock",
		"Last_name":"Bro",
		"age":20,
		"livingCity":"Tianjin",
	}

TomLee = {
		"First_name":"Tom",
		"Last_name":"Lee",
		"age":44,
		"livingCity":"Shanghai",
	}

PualBaker = {
		"First_name":"Paul",
		"Last_name":"Baker",
		"age":11,
		"livingCity":"Hongkong",
	}
people = [LockBro, TomLee, PualBaker]

for person in people:
    print(person["First_name"] + person["Last_name"] +
                " is a " + str(person["age"]) + " year's old person" +
                    " who is living in " + person["livingCity"] + ".")
