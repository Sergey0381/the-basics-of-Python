'''
--------------------------------------------------  1  -----------------------------------------------------------------

n_1 = int(input('Enter number :'))
n_2 = int(input('Enter number :'))

def my_f(n_1 ,n_2):
    try:
        return n_1 / n_2
    except ZeroDivisionError:
        print('delenie na zero')
        return
print(my_f(n_1,n_2))

--------------------------------------------------  2  -----------------------------------------------------------------

def person(surname, name, age, year, city, email, phone):

    return
surname = input('Вевдите свою фамилию:')
name = input('Вевдите своё имя:')
age = int(input('Введите свой возраст:'))
year = int(input('Введите свой год рождения:'))
city = input('Введите город по прописке :')
email = input('Ваша электронная почта:')
phone = input('Введите свой контактный телефон:')


print('Фамилия:',surname,';''Имя:',name,';''возраст:',age,'лет'';','Город:',city,';''Электронный адрес:', mail,';''Контактный телефон:',phone)

--------------------------------------------------  3  -----------------------------------------------------------------

def my_func(a, b, c):
    order = [a, b, c]
    total = []
    max_1 = max(sequence) # первый максимального значения
    total.append(max_1) # добавление перевого максимального значения
    order.remove(max_1) # вырезаем первый максимальный элемент
    max_2 = max(order) # второй максималного элемента
    total.append(max_2) # добавление второго мксимального элемента
    print(sum(total))
my_func(-8, 4, 0)

--------------------------------------------------  4  -----------------------------------------------------------------

def my_func(x, y):         # Создаём функцию принимающую два аргумента

    return 1 / x ** abs(y)# (abs)Возвращает абсолютную величину для переданного аргумента x
    #return x ** y          # Возводим в степень

print(my_func(40, 5))       # Задаём значение


--------------------------------------------------  5  -----------------------------------------------------------------

import sys

result = 0
while True:
    line = input("Enter number or special token q fo exite: ") # Запрашиваем ввод
    tokens = line.split(" ")     # Возвращаем список строк
    for token in tokens:
        try:                     # исключение
            number = float(token)
            result += number
        except:
            if token == 'q':     # проверка
                print(f"You sum is {result}. Program is terminated")
                exit(0)
            else:
                print(f"You sum is {result}. Input error", file=sys.stderr)
                exit(1)
print(result)
exit()

------------------------------------------------------------------------------------------------------------------------
'''

















