"""
9-12 多个模块 ：

将 User 类存储在一个模块中，并将 Privileges 和 Admin 类存储在另一个模块中。
再创建一个文件，在其中创建一个 Admin 实例，并对其调用方法 show_privileges() ，
以确认一切都依然能够正确地运行。
"""
import Privileges_Admin

theFirstUser = Privileges_Admin.Admin("Lock", "Bro", "male", "20", 30)
theFirstUser.Privileges.show_privileges()
