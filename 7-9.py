"""
7-9

1.继续使用7-8的sanwich_order并确保"pastrami"出现了三次
2.在程序开头说明pastrami卖完了，在使用一个while循环把sanwich_order中pastrami全部删除
3.确认最终的列表finish_sanwich中不包含pastrami
"""

sandwich_orders = ["tuna", "pastrami", "club", "pastrami", "scotch", "pastrami"]
finish_sanwiches = []

print("Sorry,the pastrami sanwich has been sold out.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    making_sanwich = sandwich_orders.pop()
    print("i made you " + making_sanwich + ".")
    finish_sanwiches.append(making_sanwich)

for sanwich in finish_sanwiches:
    print(sanwich, end=',')
