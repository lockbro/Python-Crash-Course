"""
7-8

1.创建一个名为sandwich_orders的列表，其中包括各种三明治的名字。之后再创建一个
finisher_sanwiches的空列表。
2.遍历sanwich_oeders，对于其中的每种三明治都打印一条信息，比如"i made you tuna sanwich."并讲其
移到列表finish_sanwiches。
3.所有三明治做好之后打印一条信息，将这些三明治列出来。
"""

sandwich_orders = ["tuna", "club", "scotch"]
finish_sanwiches = []

while sandwich_orders:
    making_sanwich = sandwich_orders.pop()
    print("i made you " + making_sanwich + ".")
    finish_sanwiches.append(making_sanwich)

for sanwich in finish_sanwiches:
    print(sanwich, end=',')
