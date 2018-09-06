"""
9-11 导入 Admin 类 ：

以为完成练习 9-8 而做的工作为基础，
将 User 、 Privileges 和 Admin 类存储在一个模块中，
再创建一个文件，在其中创建一个 Admin 实例
并对其调用方法 show_privileges() ，以确认一切都能正确地运行。
"""

from Admin_Privileges_User import Admin

theFirstUser = Admin("Lock", "Bro", "male", "20", 30)
theFirstUser.Privileges.show_privileges()
