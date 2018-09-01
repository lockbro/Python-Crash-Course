"""6-10

1.创建一个cities的字典，三个城市为键，
2.每个城市创建一个字典，包含所属国家country、人口population以及一个有关城市的事实fact
3.最后将城市的信息都打印出来
"""
cities = {
	"Beijing":{
		"country": "China",
		"population":2173,
		"fact":"Beijing is the capital of China.",
	},

	"Washington, D.C":{
		"country":"America",
		"population":68.1,
		"fact":"Washington, D.C is the capital of America.",
	},

	"Ottawa":{
		"country":"Canada",
		"population":132,
		"fact":"Ottawa is the capital of Canada.",
	},
}

for city, info in cities.items():
	print(city + " is the capital of " + info["country"] +
		          " and it's population is about " + str(info["population"]) +
		                  ". And the fact of this city is that " +
                                info["fact"] + "\n")
