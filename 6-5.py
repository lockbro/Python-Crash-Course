""""
6-5

1.创建一个字典，存储三条河流以及流经的国家：“nile”：“egypt”
2.使用循环为每条河流打印一条信息：”the nile run through egypt“
3.使用循环将每条河流的名字都打印出来
4.使用循环将字典包括的每个国家的名字都打印出来
"""

river_dict = {
	"Donau" : "German",
	"Thames" : "England",
	"Volga" : "Russian ",
}

for river_name, river_nation in river_dict.items():
	print("The " + river_name + " run through " + river_nation + "." )

for river in river_dict.keys():
	print(river)

for nation in set(river_dict.values()):
	print(nation)

