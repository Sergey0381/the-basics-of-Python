# task 5

profit = int(input('Ваша выручка :'))
expenses = int(input('Ваши издержки :'))

if profit > expenses:
    print('Ваша прибыль составила', '{:.2f}'.format(profit - expenses))
    personal = int(input('Количество работников? : '))
    zp = (profit - expenses) / personal
    print('Прибыль фирмы в расчёте на одного сотрудника', '{:.2f}'.format(zp), 'руб.')
else:
    print('Ваш убыток', 'руб.', '{:.2f}'.format(expenses - profit))

