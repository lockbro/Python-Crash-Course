"""
9-10 导入 Restaurant 类 ：

将最新的 Restaurant 类存储在一个模块中。
在另一个文件中，导入 Restaurant 类，创建一个 Restaurant 实例，并调
用 Restaurant 的一个方法，以确认 import 语句正确无误。
"""
from restaurant import Restaurant

theFirstRestaurant = Restaurant("yangquan", "chuan")
theFirstRestaurant.describe_restaurant()
