from user import User


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
