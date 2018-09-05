"""
9-6 冰淇淋小店 ：

冰淇淋小店是一种特殊的餐馆。
编写一个名为 IceCreamStand 的类，让它继承你为完成练习 9-1 或练习 9-4 而编写的 Restaurant 类。
这两个版本的 Restaurant 类都可以，挑选你更喜欢的那个即可。
添加一个名为 flavors 的属性，用于存储一个由各种口味的冰淇淋组成的列表。
编写一个显示这些冰淇淋的方法。创建一个 IceCreamStand 实例，并调用这个方法。
"""


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("This restaurant's name is " + self.restaurant_name +
              ", and it specialize in " + self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is opening")

    def set_number_served(self, set_number):
        self.number_served = set_number

    def increment_number_served(self, increment_number, total_number):
        if self.number_served <= total_number:
            self.number_served += increment_number
        else:
            print("Sorry , we don't recepte guest any more.")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Chocolate", "Coconut", "Vanilla", "Mango", "Taro"]


IceCreamStand = IceCreamStand("Häagen-Dazs", "IceCream")

print(IceCreamStand.flavors)
