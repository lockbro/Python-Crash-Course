"""6-9
1.创建一个favorite_places的字典，将三个人的名字作为键
2.对于其中的每个人都存三个他喜欢的地方。
3.遍历这个字典将这些信息打印出来
"""

favorite_place = {
	"Tom": ["Nanning", "Beijing", "Shanghai"],
	"Jack": ["Hongkong", "Tailand", "Xian"],
    "Mike": ["Sichuan", "Wuhan", "Suzhou"],
}

for person, place in favorite_place.items():
	print(person + "'s favorite place is : " + ",".join(place) + ".")
