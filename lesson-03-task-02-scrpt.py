# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

from random import randint

SIZE = 5
LOW_VAL = 0
HGH_VAL = 100

massiv = [randint(LOW_VAL, HGH_VAL) for _ in range(SIZE)]
print(massiv)

massiv_new = []

for i in range(SIZE):
    if massiv[i] % 2 == 0:
        massiv_new.append(i)

print(massiv_new)
