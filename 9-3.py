"""
9-3 用户 ：

创建一个名为 User 的类，
其中包含属性 first_name 和 last_name ，还有用户简介通常会存储的其他几个属性。
在类 User 中定义一个名为 describe_user() 的方法，它打印用户信息摘要；
再定义一个名为 greet_user() 的方法，它向用户发出个性化的问候。
创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
"""


class User():
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def describe_user(self):
        print(self.first_name + self.last_name + " is a " +
              self.age + " years old " + self.gender)

    def greet_user(self):
        print("Hello " + self.first_name + self.last_name)


theFirstUser = User("Lock", "Bro", "male", "29 yr")
theSecondUser = User("Jay", "Chou", "male", "30yr")
theThirdUser = User("Adele", "Adkins", "female", "30yr")

theFirstUser.describe_user()
theFirstUser.greet_user()

theSecondUser.describe_user()
theSecondUser.greet_user()

theThirdUser.describe_user()
theThirdUser.greet_user()
