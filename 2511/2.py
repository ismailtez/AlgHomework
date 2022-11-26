""" Алгоритм имеет 1 цикл поэтому сложность O(n) """

def getMaximumGenerated(n):
    number = [0] * (n + 1)  # Задаем переменную со списком нулей кол-во которых определяется от задаваемого значения n+1
    number[1] = 1
    for i in range(1, len(number)):  # реализуем заполнение как представлено в задании
        if 2 <= 2 * i <= n:
            number[2 * i] = number[i]
        if 2 <= 2 * i + 1 <= n:
            number[2 * i + 1] = number[i] + number[i + 1]
    return max(number)  # возврат максимального элемента


print(getMaximumGenerated(5))
