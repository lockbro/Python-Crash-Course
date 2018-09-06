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
