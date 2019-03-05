mytuple = (1, 2, 3)
mydict_1 = {'apple': 30, 'banana': 40, 'orange': 38}
mydict_2 = {'grapes': 30, 'banana': 50, 'orange': 28}
mycombo = {**mydict_1, **mydict_2}  # merging two dictionary
ex_dict = {'x': 1, 'y': 2, 'z': 3}


# print(mycombo) #{'apple': 30, 'banana': 50, 'orange': 28, 'grapes': 30}
# print(x)  # (1, 2, 3)
# print(y)  # {'apple': 30, 'banana': 40, 'orange': 38}
# print(*x)  # 1 2 3
# print(**y)  # will show error as invalid keyword passed

def myprint(x, y, z):
    print(x, y, z)


# myprint(*mytuple)
# myprint(**ex_dict) # to unpack a dictionary keys should be similar

add = (lambda x, y: x + y)
# print(add(4, 5))

apple_value, banana_value = (lambda apple, banana, **_: (apple, banana))(
    **mycombo)  # **_ will skip whatever keys will after that
# print(apple_value, banana_value)
