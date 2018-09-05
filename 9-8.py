"""
9-8 权限 ：

编写一个名为 Privileges 的类，它只有一个属性 —— privileges ，其中存储了练习 9-7 所说的字符串列表。
将方法 show_privileges() 移到这个类中。
在 Admin 类中，将一个 Privileges 实例用作其属性。
创建一个 Admin 实例，并使用方法 show_privileges() 来显示其权限
"""


class User():
    def __init__(self, first_name, last_name, gender, age, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        print(self.first_name + self.last_name + " is a " +
              self.age + " years old " + self.gender)

    def greet_user(self):
        print("Hello " + self.first_name + self.last_name)

    def increment_number_served(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges():
    def __init__(self, privileges=["can add post",
                                   "can delete post",
                                   "can ban user"]):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print("Administrator " + privilege)


class Admin(User):
    def __init__(self, first_name, last_name, gender, age, login_attempts):
        super().__init__(first_name, last_name, gender, age, login_attempts)
        self.Privileges = Privileges()


Admin = Admin("Lock", "Bro", "male", "20", "10")
Admin.Privileges.show_privileges()
