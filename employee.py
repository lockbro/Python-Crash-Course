class Employee():
    def __init__(self, FirstName, LastName, SalaryOfYear=0):
        self.FirstName = FirstName
        self.LastName = LastName
        self.SalaryOfYear = SalaryOfYear

    def give_raise(self, salary_puls=5000):
        self.SalaryOfYear += salary_puls
        return self.SalaryOfYear


one = Employee('xiao', 'zhan', 80000)
number = one.give_raise()
