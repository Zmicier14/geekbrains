# Удаление элемента из списка во время его итерации
#
# list_1 = [1, 2, 3, 4]
# list_2 = [1, 2, 3, 4]
# list_3 = [1, 2, 3, 4]
# list_4 = [1, 2, 3, 4]
#
# for i, item in enumerate(list_1):
#     del item
#
# print(list_1)
#
# for i, item in enumerate(list_2):
#     list_2.remove(item)
#
# print(list_2)
#
# for i, item in enumerate(list_3):
#     list_3.pop(i)
#
# print(list_3)
#
# for i, item in enumerate(list_4[:]):
#     list_4.remove(item)
#
# print(list_4)

# Крестики-нолики, где Х побеждает с первого раза

# row = [''] * 3
# board = [row] * 3
# print(board)
# board[1][1] = 'X'
# print(board)
# board = [[''] * 3  for _ in range(3)]
# print(board)
# board[0][0] = 'X'
# print(board)

# Те же опернады, но другая история
# a = [1, 2, 3, 4]
# b = a
# a = a + [5, 6, 7]
# print(a, b)
#
# a = [1, 2, 3, 4]
# b = a
# a += [5, 6, 7]
# print(a, b)

# Игла в стоге сена
# a = ('one', 'two', 'three')
# for i in a:
#     print(i)
#
# a = ('one',)
# for i in a:
#     print(i)

# Сохранить только уникальные значения
# lst = [1, 2, 7, 3, 5, 6, 1, 3, 8, 9]
# lst = list(set(lst))
# print(lst)

# Ключ словаря - изменяемый объект
set_x = {1, 2, 6}
lst_x = [5, 6, 9]
#dict_x = {set_x: lst_x}
#dict_x = {lst_x: set_x}
dict_x = {frozenset(set_x): lst_x}
dict_y = {tuple(lst_x): set_x}
print((dict_x))
print(dict_y)