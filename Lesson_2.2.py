#Задание 2

m_list = list(input('Ввод')) # - Запарашиваем значения
for i in range(1, len(m_list),2): # - 1 индекс элемента, 2 шаг прохода
    m_list[i - 1], m_list[i] = m_list[i], m_list[i - 1] #  - i номер элемента
    print(m_list)