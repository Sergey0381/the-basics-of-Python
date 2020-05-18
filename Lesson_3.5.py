#Task  5

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
