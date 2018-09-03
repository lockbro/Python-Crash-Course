"""
9-2 三家餐馆 ：

根据你为完成练习 9-1 而编写的类创建三个实例，
并对每个实例调用方法 describe_restaurant() 。
"""


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("This restaurant's name is " + self.restaurant_name +
              ", and it specialize in " + self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is opening")


theFirstRestaurant = Restaurant("yangquan", "chuan")
theSecondRestaurant = Restaurant("guangzhou", "yue")
theThirdRestaurant = Restaurant("jixiang", "lu")
theFirstRestaurant.describe_restaurant()
theSecondRestaurant.describe_restaurant()
theThirdRestaurant.describe_restaurant()
