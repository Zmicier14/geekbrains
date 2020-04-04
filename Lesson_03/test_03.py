# Сортировка чисел массива на массивы с отрицательными числами и положительными

import random

array = [random.randint(-100, 100) for _ in range(100)]
print(array)

arr_below = []
arr_lager = []

for item in array:
    if item > 0:
        arr_below.append(item)
    elif item < 0:
        arr_lager.append(item)

print(arr_below)
print(arr_lager)