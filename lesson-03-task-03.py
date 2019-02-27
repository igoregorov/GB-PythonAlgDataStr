# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

SIZE = 10
LOW_VAL = 0
HGH_VAL = 100

massiv = [randint(LOW_VAL, HGH_VAL) for _ in range(SIZE)]

min_elem = massiv[0]
max_elem = massiv[SIZE]

for i in range(SIZE):
    min_elem = massiv[i] if massiv[i] < min_elem else min_elem
    max_elem = massiv[i] if massiv[i] > max_elem else max_elem

print("Max: ", max_elem, "Min: ", min_elem)
