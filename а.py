summa = 0
kol = 0
vvod = input("Введите целое число или слово «стоп»: ")
while vvod != "стоп":
    summa = summa + int(vvod)
    kol = kol + 1
    vvod = input("Введите целое число или слово «стоп»: ")
    

print("Сумма чисел:", summa / kol)