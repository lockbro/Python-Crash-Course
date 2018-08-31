"""6-8

1.创建多个字典每个字典都用一个宠物的名称来命名；
2.在每个字典中要包含宠物的类型以及主人的名字
3.将这个字典纯在一个名为pets的列表中
3.遍历列表，将宠物的信息打印出来

"""
Tom = {
	"pet_name" : "Tom",
	"pet_type" : "cat",
	"pet_master" : "LockBro",
}

Jerry = {
	"pet_name" : "Jerry",
	"pet_type" : "mouse",
	"pet_master" : "PaulBaker",
}

Angel = {
	"pet_name" : "Angel",
	"pet_type" : "dog",
	"pet_master" : "TomLee",
}

pets = [Tom, Jerry, Angel]

for pet in pets:
    print(pet["pet_name"] + " is a " + pet["pet_type"] +
			 ",and her master's name is " +
			 pet["pet_master"] + ".")
