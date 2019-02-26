# 4. Определить, какое число в массиве встречается чаще всего.


from random import randint

SIZE = 100
LOW_VAL = 0
HGH_VAL = 10

massiv = [randint(LOW_VAL, HGH_VAL) for _ in range(SIZE)]

print(massiv)

# Используется один проход по массиву. Выделяется памяти на диапозон чисел в массиве -
# это оптимально, если диапозон чисел меньше размера массива.

# здесь храним значение элемента, который самый частый, и его частоту
# можно и две отдельные переменные использовать
max_freq = [massiv[0], 1]

# в памяти массив с частотами элементов
freq_max = [0 for _ in range(LOW_VAL, HGH_VAL+1)]

for i in range(0, SIZE):
    freq_max[massiv[i]-LOW_VAL] += 1
    if max_freq[1] < freq_max[massiv[i]-LOW_VAL]:
        max_freq[1] = freq_max[massiv[i]-LOW_VAL]
        max_freq[0] = massiv[i]

print(max_freq[0], "-", max_freq[1])

# второй вариант, с двумя проходами по массиву, но в памяти только элемент
# начинаем с начала, и для каждого элемента считаем его частоту
# вторым проходом, от текущей поиции, до конца массива
freq = 1
index = 1
max_freq = 0
for i in range(SIZE-1):
    for j in range(i+1, SIZE):
        if massiv[i] == massiv[j]: freq += 1
    if freq > max_freq:
        max_freq = freq
        index = i
    freq = 1

print(massiv[index], "-", max_freq)

# отличие первого алгоритма от второго, что при рваных частотах,
# первый возьмет последнее число, а второй - первое встретившееся
