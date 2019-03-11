# import memory_profile
# сволочь, хочет visual c v14 - а я не со своего компа :(
from random import randint
import sys


# примерно то же, что на уроке, только сразу выводим размер массива... если он одномерный :))))
def show_sizeof(x):

    summa_x = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                summa_x += sys.getsizeof(xx)
        else:
            for xx in x:
                summa_x += sys.getsizeof(xx)

    return summa_x


SIZE = 15
LOW_VAL = 0
HGH_VAL = 100

massiv = [randint(LOW_VAL, HGH_VAL) for _ in range(SIZE)]

print("SIZE:", show_sizeof(SIZE))
print("LOW_VAL:", show_sizeof(LOW_VAL))
print("HGH_VAL:", show_sizeof(HGH_VAL))
print("massiv:", show_sizeof(massiv))

min_elem = [massiv[0], 0]
max_elem = [massiv[SIZE-1], SIZE-1]

print("min_elem:", show_sizeof(min_elem))
print("max_elem:", show_sizeof(max_elem))

# print(massiv)

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

# print("Max: ", max_elem[0], "Min: ", min_elem[0])

massiv[min_elem[1]], massiv[max_elem[1]] = massiv[max_elem[1]], massiv[min_elem[1]]
# print(massiv)

print("massiv:", show_sizeof(massiv))


# variant2
import array

massiv2 = array.array('i', [randint(LOW_VAL, HGH_VAL) for _ in range(SIZE)])

print("massiv2:", show_sizeof(massiv2))

massiv3 = array.array('i', [randint(LOW_VAL, HGH_VAL) for _ in range(0)])
massiv4 = [randint(LOW_VAL, HGH_VAL) for _ in range(0)]

print("massiv3:", show_sizeof(massiv3))
print("massiv4:", show_sizeof(massiv4))

massiv5 = array.array('i', [randint(LOW_VAL, HGH_VAL) for _ in range(1000)])
massiv6 = [randint(LOW_VAL, HGH_VAL) for _ in range(1000)]

print("massiv5:", show_sizeof(massiv5))
print("massiv6:", show_sizeof(massiv6))


# SIZE: 28
# LOW_VAL: 24
# HGH_VAL: 28
# massiv: 600
# min_elem: 124
# max_elem: 128
# massiv: 600
# massiv2: 544

# -------- 2 элемента ------
# massiv3: 64 --- array
# massiv4: 56

# -------- 1000 элементов ------
# massiv5: 32020 --- array
# massiv6: 36976

# Вывод, вообще, непонятно, зачем брать действующую программу. Сосредоточился на сравнении списка и массива из array
# при большом количестве элементов, array выгоднее по памяти. А на двух элементах, array больше места забирает.
# Вот в последнем примере, на 1000 элементов выигрыш в 4кб.