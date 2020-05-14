#task 2

sec = int(input('Введите время в секундах: '))

hours = sec // 3600
minutes = (sec - hours * 3600) // 60
seconds = sec % 60
print("{:.2f} часы:{:.2f} минуты:{:.2f} секунды: ".format(hours, minutes, seconds))