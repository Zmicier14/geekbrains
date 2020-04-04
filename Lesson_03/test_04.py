# Вставляем элемент в определенную позицию массива

import random

array = [random.randint(0, 100) for _ in range(100)]
print(array)

num = int(input('Enter the number to add: '))
pos = int(input('Enter the position of array to add: '))
# version 1:
#
# array.append(None)
# i = len(array) - 1
#
# while i > pos:
#     array[i], array[i - 1] = array[i - 1], array[i]
#     i -= 1
#
# version 2:
#
# array.insert(pos, num)
#
# version 3
array_new = array[:pos] + [num] + array[pos:]

array[pos] = num
print(array)