"""
11-3 雇员 ：

编写一个名为 Employee 的类，其方法 __init__() 接受名、姓和年薪，并将它们都存储在属性中。
编写一个名为 give_raise() 的方法，它默认将年薪增加 5000 美元，但也能够接受其他的年薪增加量。

为 Employee 编写一个测试用例，
其中包含两个测试方法： test_give_default_raise() 和 test_give_custom_raise() 。
使用方法 setUp() ，以免在每个测试方法中都创建新的雇员实例。
运行这个测试用例，确认两个测试都通过了。
"""


import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.origion_salary = 80000
        self.default_raise = 5000
        self.new_number = 6000
        self.default = Employee("lock", "bro", self.origion_salary)

    def test_give_default_raise(self):
        current_salary = self.default.give_raise()
        self.assertEqual(
            current_salary, (self.origion_salary + self.default_raise))

    def test_give_custom_raise(self):
        current_salary = self.default.give_raise(self.new_number)
        self.assertEqual(
            current_salary, (self.origion_salary + self.new_number))


unittest.main()
