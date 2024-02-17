f = open('data2.txt', 'r', encoding="utf-8")
str1 = f.readline().strip()
str1 = int(str1)
print("Сейчас денег там:", str1)
f.close()

rt = input("что сделать?:")
if rt == "просто закрыть файл":
    f.close
elif rt == "прибавить число":
    e = int(input())
    str1 = str1 + e
elif rt == "убавить число":
    r = int(input())
    str1 = str1 - r
    
f = open('data2.txt', 'w', encoding="utf-8")
str1 = str(str1)
f.write(str1)
f.close()