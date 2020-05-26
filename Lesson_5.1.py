# Task 1

my_f = open('test.txt', 'w') # открываем файл на запись
line = input('введите данные \n') # Запрос ввода
while line: # запускаем цикл
    my_f.writelines(line) # читаем строки
    line = input('введите данные \n')
    if not line:
        break # Прерывание цикла

my_f.close() # Закрываем файл
my_f = open('test.txt', 'r') # открываем файл на чтение
content = my_f.readlines()
print(content)
my_f.close()

