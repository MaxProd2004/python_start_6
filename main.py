# Задание 1
print("Задание 1")
st_1 = str(input("Введите строку текста: "))
num_of_b = 0
for i in list(st_1):
    if 'b' in i:
        num_of_b += 1
print("Количество букв 'b' в строке текста: ", num_of_b, '\n')

# Задание 2
print("Задание 2")
name = str(input("Введите имя: "))
firstLetterIsBig = bool(name[0].istitle())
onlyLettersInName = bool(name.isalpha())
if firstLetterIsBig == False:
    print("Неккоректное имя: написано с маленькой буквы!\n")
if onlyLettersInName == False:
    print("Неккоректное имя: недопустимые символы в имени!\n")
else:
    print(name, '\n')

# Задание 3
print("Задание 3")
st_2 = str(input("Введите любую строку: "))
listOfOrds = []
for i in st_2:
    listOfOrds.append(ord(i))
print("Сумма кодов символов строки: ", sum(listOfOrds), '\n')

# Задание 4
print("Задание 4")
from math import pi
number_of_places = 1
while number_of_places <= 10:
    number_of_places += 1
    print('{:.{}f}'.format(pi, number_of_places))
print('\n')

# Задание 5
print("Задание 5")
st_3 = (input("Введите строку слов, разделенных пробелами: ").split())
print(max(st_3, key=len))
