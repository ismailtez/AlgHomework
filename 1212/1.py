"""
Сложность O(n) т.к. зависит от длины задаваемого односвязного списка.
Функция возвращает True или False в зависимости от того,
является ли список палиндромом
"""

from typing import Optional, List

class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrom(head: Optional[ListNode]) -> bool:
    arr, cur = [], head     # Создание перемен массива и текущего элемента.
    while cur:              # Переводим список в массив.
        arr.append(cur.val) # К массиву добавляем значение текущего элемента списка.
        cur = cur.next      # Переходим на следующий элемент списка.
    return arr == arr[::-1] # Возвращает True если это палиндром и False если нет.
