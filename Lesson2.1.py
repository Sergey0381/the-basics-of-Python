

'''

#Задание 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
m_list = (2 , None, 'ffg' , 5.6 , True, False, (4,3),{4,3}) # -  Значения для обработки
for i in  [m_list][0]: # проходим в цикле по индексам
     print(type(i))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Задание 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
m_list = list(input('Ввод')) # - Запарашиваем значения
for i in range(1, len(m_list),2): # - 1 индекс элемента, 2 шаг прохода
    m_list[i - 1], m_list[i] = m_list[i], m_list[i - 1] #  - i номер элемента
    print(m_list)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Задание 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
user_str = input('Введите строки через пробел: ')
str_list = user_str.split() # Разбиваем строку на части и возвращаем список

for i, word in enumerate(str_list): # Генерим кортеж
    print(f'{i + 1}) {word[:10]}')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Задание 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ratings = [22, 10, 4]


while True:

    rating = input('Введите новое значение рейтинга: ')




    try:

        rating = abs(int(rating))

    except ValueError as e:

        print('Ошибка ввода')

        continue




    #rating еще не встречался в списке

    if not ratings.count(rating):

        #вставляем впереди или вконце списка

        if rating > ratings[0]:

            ratings.insert(0, rating)

        elif rating < ratings[-1]:

            ratings.append(rating)

        # ищем куда можем вставить внутри списка

        else:

            for k, v in enumerate(ratings):

                if rating > v:

                    ratings.insert(k, rating)

                    break

    #уже есть такое значение

    else:

        new_index = ratings.index(rating) + ratings.count(rating)

        ratings.insert(new_index, rating)




    print(ratings)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''