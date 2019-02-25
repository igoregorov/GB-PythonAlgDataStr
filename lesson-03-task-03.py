# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import random

LOW_VAL=-10
HGH_VAL=10

n = int(input("Введите размер массива: "))
a = []
for i in range(n):
    a.append(int(LOW_VAL - 1 + (HGH_VAL - LOW_VAL + 2) * random()))

#print(a)

min_elem = a[0]
max_elem = a[n-1]

for i in range(n):
    if a[i] < min_elem: min_elem = a[i]
    elif a[i] > max_elem: max_elem = a[i]

print("Max: ", max_elem, "Min: ", min_elem)
