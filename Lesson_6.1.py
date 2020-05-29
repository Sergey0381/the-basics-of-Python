# Task 1

from time import sleep # Импорт библиотеки


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый', 'Оранжевый','О'] #__ Приватное использование значений

    def running(self): # Создаём функцию
        i = 0
        while i <= 4: # Создаём цикл
            print(f'Светофор переключается \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            elif i == 3:
                sleep(3)
            elif i == 4:
                sleep(7)
            i += 1


TrafficLight = TrafficLight() # Создаём переменную
TrafficLight.running() # Вызываем фкнкцию
