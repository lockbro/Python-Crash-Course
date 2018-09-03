"""
8-14 汽车 ：

编写一个函数，将一辆汽车的信息存储在一个字典中。
这个函数总是接受制造商和型号，还接受任意数量的关键字实参。

这样调用这个函数：提供必不可少的信息，以及两个名称 — 值对，如颜色和选装配件。
这个函数必须能够像下面这样进行调用：
car = make_car('subaru', 'outback', color='blue', tow_package=True)
"""


def make_car(manufacturer, model, **other_info):
    car_dict = {}
    car_dict["manufacturer"] = manufacturer
    car_dict["model"] = model
    for key, value in other_info.items():
        car_dict[key] = value
    return car_dict


car = make_car('subaru', 'outback', color='blue', tow_package=True, GPS=True)
print(car)
