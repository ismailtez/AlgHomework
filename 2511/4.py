"""Сложность  O(n) т.к. она зависит от длины задаваемого массива.
Функция проходится по массиву с ценами сравнивая каждое значение массива,
если значение больше предыдущего, то оно записывается в счетчик прибыли.
"""

def maxProfit(price):
    count = 0                                # Переменная,счетчик прибыли
    for i in range(1, len(price)):          # Проходимся по длине списка с ценами от 1 до конца
        if price[i] > price[i-1]:          # Проверка, если цена больше предыдущей
            count += price[i] - price[i-1] # То к переменной прибавляем разность этой и предыдущей цены
    return count

print(maxProfit([8, 2, 6, 4, 7, 5, 10, 12, 14]))
