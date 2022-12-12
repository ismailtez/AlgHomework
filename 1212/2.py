"""
Сложность  O(n) т.к. зависит от длины задаваемого односвязного списка
Функция из двоичного представления значений в односвязном списке возвращает в десятичном виде.
"""

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue(head: ListNode) -> int:
    head_list = head               # Переменной присваиваем односвязный список.
    none = ''                       # Переменой none присваивается пустая строка.
    while head_list:               # Проходимся по списку.
        none += str(head_list.val)  # переменной none присваиваем значение односвязного списка в строковом типе данных.
        head_list = head_list.next  # Переходим на следующий элемент списка.
    return(int(none,2))             # Возвращает значение переменной none в десятичном виде.
