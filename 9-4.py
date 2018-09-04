"""
9-4 就餐人数 ：

在为完成练习 9-1 而编写的程序中，添加一个名为 number_served 的属性，并将其默认值设置为 0 。
根据这个类创建一个名为 restaurant 的实例；
打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
添加一个名为 set_number_served() 的方法，它让你能够设置就餐人数。
调用这个方法并向它传递一个值，然后再次打印这个值。
添加一个名为 increment_number_served() 的方法，它让你能够将就餐人数递增。
调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
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


restaurant = Restaurant("Yangquan", "chuan")
print("The are " + str(restaurant.number_served) +
      " guests in the restaurant.")

restaurant.number_served = 8

print("The are " + str(restaurant.number_served) +
      " guests in the restaurant.")

restaurant.set_number_served(5)

print("There are " + str(restaurant.number_served) +
      " guests in the restaurant.")

restaurant.increment_number_served(4, 100)
