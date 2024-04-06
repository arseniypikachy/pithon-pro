import random
x = input("1,камень 2,ножницы 3,бумага:")
if x == "1":
    print("камень")
elif x == "2":
    print("ножницы")
elif x == "3":
    print("бумага")
z = str(random.randint(1,3))
if z == "1":
    print("камень")
elif z == "2":
    print("ножницы")
elif z == "3":
    print("бумага")
if x == "1":
    if z == "2":
        print("x выиграл")
    elif z == "3":
        print("z выиграл")
    elif z == "1":
        print("ничья")
elif x == "2":
    if z == "1":
        print("z выиграл")
    elif z == "2":
        print("ничья")
    elif z == "3":
        print("x выиграл")
elif x == "3":
    if z == "1":
        print("x выиграл")
    elif z == "2":
        print("z выиграл")
    elif z == "3":
        print("ничья")