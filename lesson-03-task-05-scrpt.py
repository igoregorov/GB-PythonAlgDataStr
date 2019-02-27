# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве

from random import randint

SIZE = 10
LOW_VAL = 0
HGH_VAL =  5

massiv = [randint(LOW_VAL, HGH_VAL) for _ in range(SIZE)]
print(massiv)

# ничего более оптимального в голову не приходит :(
maxEL = 0
posEL = -1

for i in range(SIZE):
    if massiv[i] < 0:
        if maxEL < massiv[i] or maxEL == 0:
            maxEL = massiv[i]
            posEL = i

print(f'{maxEL} at position {posEL}') if posEL >= 0 else print("Нет отрицательных элементов")

