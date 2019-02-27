# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randint

SIZE = 7
LOW_VAL = 0
HGH_VAL = 10

massiv = [randint(LOW_VAL, HGH_VAL) for _ in range(SIZE)]

#massiv = [7, 0, 1, 8, 8, 8, 1]
print(massiv)

a, b = (0, 1) if massiv[0] < massiv[1] else (1, 0)
min1 = dict(value=massiv[a], position=a)
min2 = dict(value=massiv[b], position=b)


# Фффухххх
# по сравнению с тем, что было в начале - Небо и Земля :)
for i in range(2, SIZE):
    if min1.get('value') > massiv[i]:
        min2 = min1
        min1 = dict(value=massiv[i], position=i)
# вот это второе условие, я почему-то пытался обходить дополнительными сравнениями в первом.
# хотя в голове сидела картинка двух человечков, которые идут по горам
    if min2.get('value') > massiv[i] and min1.get('position') != i:
        min2 = dict(value=massiv[i], position=i)


print(f'min1: {min1} ')
print(f'min2: {min2} ')

# Второй вариант тупой - двухпроходный, даже писать его не буду
