# Бинарный поиск числа в массиве
import random

def bin_search(array, value):

    left = 0
    right = len(array) - 1
    pos = (left + right) // 2

    while left <= right and array[pos] != value:
        if value > array[pos]:
            left = pos + 1
        else:
            right = pos - 1

        pos = (left + right) // 2

    return -1 if left > right else pos

a = [random.randint(0, 1000) for _ in range(100)]
a.sort()
print(a)

n = int(input('Enter the search number: '))
print(bin_search(a, n))