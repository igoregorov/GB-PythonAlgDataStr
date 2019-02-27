# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

# Здесь в задаче не добавлено условие, что при равных элементах брать наиболее адленные друг от друга
# А жаль, было бы интересно :)

from random import randint

SIZE = 8
LOW_VAL = 0
HGH_VAL = 20

massiv = [randint(LOW_VAL, HGH_VAL) for _ in range(SIZE)]

print(massiv)

min_elem_pos = max_elem_pos = 0
min_elem = max_elem = massiv[0]

for i in range(SIZE):
    # если массив состоит из одинаковых элементов, то сумма будет равна нулю
    if massiv[i] <= min_elem:
        min_elem = massiv[i]
        min_elem_pos = i
    elif massiv[i] >= max_elem:
        max_elem = massiv[i]
        max_elem_pos = i

print(f'min: {min_elem} at {min_elem_pos}')
print(f'max: {max_elem} at {max_elem_pos}')

# через step в функции range играть дольше
min_elem_pos, max_elem_pos = (max_elem_pos, min_elem_pos) if min_elem_pos > max_elem_pos \
                        else (min_elem_pos, max_elem_pos)

summa = 0
for i in range(min_elem_pos+1, max_elem_pos): summa += massiv[i]

print(f'summa : {summa}')
