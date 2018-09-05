"""
9-7 管理员 ：

管理员是一种特殊的用户。
编写一个名为 Admin 的类，让它继承你为完成练习 9-3 或练习 9-5 而编写的 User 类。
添加一个名为 privileges 的属性，用于存储一个由字符串
（如 "can add post" 、 "can delete post" 、 "can ban user" 等）组成的列表。
编写一个名为 show_privileges() 的方法，它显示管理员的权限。
创建一个 Admin 实例，并调用这个方法。
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


class Admin(User):
    def __init__(self, first_name, last_name, gender, age, login_attempts):
        super().__init__(first_name, last_name, gender, age, login_attempts)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print("Administrator " + privilege)


Admin = Admin("Lock", "Bro", "male", "20", "10")

Admin.show_privileges()
