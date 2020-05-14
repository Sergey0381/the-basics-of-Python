#Задание 5

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