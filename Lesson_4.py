"""
Lesson 4 https://github.com/Sergey0381/the-basics-of-Python/pull/5
--------------------------------------------------------- 1 ------------------------------------------------------------
from sys import argv                           # Из библиотеки sys импортируем элемент argv для ввода аргументов из cmd

name, time, salary, bonus = argv
try:                                           # Отлавливаем ошибку
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    res = time * salary + bonus                # Производим расчёт ЗП
    print(f'заработная плата сотрудника  {res}')
except ValueError:
    print('Not a number')

--------------------------------------------------------- 2 ------------------------------------------------------------

from itertools import groupby
my_list = [200, 2, 12, 73, 1, 1, 4, 10, 7, 1, 78, 123, 55, 2]
my_list.sort()
new_list = [i for i,_ in groupby(my_list)]
print(new_list)

--------------------------------------------------------- 3 ------------------------------------------------------------

print(f'Числа от 20 до 240 кратные 20 или 21 -/n'  # как в условии
 f'{[el for el in range(20, 241) if el % 20 == 0 or el  % 21 == 0]}')


print(f'Числа от 20 до 240 кратные 20 или 21 -/n' # более компактный вывод с шагом
      f'{[el for el in range(20,241,20) if el % 20 == 0 or el % 21 == 0]}')

--------------------------------------------------------- 4 ------------------------------------------------------------


my_list = [1, 4, 4, 2, 3, 2, 8, 10, 8, 5]
new_my_list = [el for el in my_list if my_list.count(el) < 2]
print(new_my_list)


--------------------------------------------------------- 5 ------------------------------------------------------------


from functools import reduce


def my_func(el_p, el):
    return el_p * el

print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

------------------------------------------------------------------------------------------------------------------------
"""
