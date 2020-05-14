#Задание 4

user_str = input('Введите строки через пробел: ')
str_list = user_str.split() # Разбиваем строку на части и возвращаем список

for i, word in enumerate(str_list): # Генерим кортеж
    print(f'{i + 1}) {word[:10]}')