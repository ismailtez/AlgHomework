""" Алгоритм имеет 1 цикл поэтому сложность O(n) """

def getMaximumGenerated(n):
    nums = [0] * (n + 1)
    nums[1] = 1
    for i in range(1, len(nums)):  # реализуем заполнение как представлено в задании
        if 2 <= 2 * i <= n:
            nums[2 * i] = nums[i]
        if 2 <= 2 * i + 1 <= n:
            nums[2 * i + 1] = nums[i] + nums[i + 1]
    return max(nums)  # возврат максимального элемента


print(getMaximumGenerated(7))
