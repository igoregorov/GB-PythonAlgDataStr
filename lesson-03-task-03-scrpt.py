# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

SIZE = 15
LOW_VAL = 0
HGH_VAL = 100

massiv = [randint(LOW_VAL, HGH_VAL) for _ in range(SIZE)]

# сознательно не ввожу более сложных структур или отдельных переменных
min_elem = [massiv[0], 0]
max_elem = [massiv[SIZE-1], SIZE-1]

print(massiv)

for i in range(SIZE):
    if massiv[i] < min_elem[0]:
        min_elem[0] = massiv[i]
        min_elem[1] = i

# по-моему, в стандартных решениях алгоритма эта ветка выполняется в любом случае
# на самом деле, если мы решили что наш элемент меньше минимального, сравнение с максимум можно не делать
# поэтому конструкция if .. elif ..
    elif massiv[i] > max_elem[0]:
        max_elem[0] = massiv[i]
        max_elem[1] = i

print("Max: ", max_elem[0], "Min: ", min_elem[0])

massiv[min_elem[1]], massiv[max_elem[1]] = massiv[max_elem[1]], massiv[min_elem[1]]
print(massiv)
