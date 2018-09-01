"""
7-10

编写一个程序，调查用户梦想的度假胜地。
使用类似于 “If you could visit one place in the world, where would you go?” 的提示，
并编写一个打印调查结果的代码块。
"""

info = {}
flag = True

while True:
    answer = input("May i ask you same question?")
    if answer == "no" or answer == "fine":
        break
    elif answer == "yes":
        name = input("What's your name : ")
        place = input("If you could visit one place in the world, \
                                where would you go : ")
        info[name] = place

for name, place in info.items():
    print(name + " want to go to the " + place)
