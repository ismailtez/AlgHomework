"""
Сложность  O(n) поскольку имеет единственный цикл.
"""

from typing import Optional, List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:
    if head == None or head.next == None:     # Если  список пуст или имеет лишь 1 значение
        return False                          # То False
    pred = head                               # Переменной "предыдущий" задается односвязный список
    curr = head.next                          # Переменной текущий присваивается следующий элемент списка
    while curr.next:                          # Создаем цикл, пока следующий элемент есть...
        curr = curr.next.next                 # Текущему элементу присваиваем значение после-следующего элемента(2 шага) списка
        pred = pred.next                      # Предыдущему элементу присваиваем значение предыдущего от текущего (1 шаг)
        if curr == pred:                      # Если текущий элемент равен предыдущему, True
            return True
        if curr == None or curr.next == None: # Если текущего элемента нет или следующего после текущего нет, то
            return False                      # False
    return False
