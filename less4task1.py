# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randint


def find_min12_v1(massiv):

    min1, min2 = (0, 1) if massiv[0] < massiv[1] else (1, 0)

    for i in range(2, len(massiv)):
        if massiv[min1] > massiv[i]:
            min2 = min1
            min1 = i
        if massiv[min2] > massiv[i] and min1 != i:
            min2 = i

    return massiv[min1], massiv[min2]


def find_min12_v2(array):
    min_first, min_second = (0, 1) if array[0] > array[1] else (1, 0)

    for i in range(2, len(array)):
        if array[i] < array[min_first]:
            spam = min_first
            min_first = i
            if array[spam] < array[min_second]:
                min_second = spam

        elif array[i] < array[min_second]:
            min_second = i

    return array[min_first], array[min_second]


def find_min12_v3(array):
    min_1 = min(array)
    array.remove(min_1)
    min_2 = min(array)

    return min_1, min_2


def test_func(func):
    lst_test = [0, 1, 2, 3, 1]
    rslt = {0, 1}
    if rslt == set(list(func(lst_test))):
        print(f'Test {func} OK')
    else: print(f'Test {func} False')


test_func(find_min12_v1)
test_func(find_min12_v2)
test_func(find_min12_v3)

# cProfile mainP
# def mainP(func, n):
#     SIZE = n
#     LOW_VAL = 0
#     HGH_VAL = n*100
#     massiv = [randint(LOW_VAL, HGH_VAL) for _ in range(SIZE)]
#
#     func(massiv)


# cProfile.run('main(find_min12_v1, 10000000)')
#         1    0.000    0.000   29.657   29.657 lesson-04-task-01.py:58(mainP)
#         1    3.646    3.646   26.918   26.918 lesson-04-task-01.py:62(<listcomp>)
#         1    2.738    2.738    2.738    2.738 lesson-04-task-01.py:7(find_min12_v1)

# cProfile.run('main(find_min12_v2, 10000000)')
#         1    0.000    0.000   29.856   29.856 lesson-04-task-01.py:67(mainP)
#         1    3.687    3.687   26.921   26.921 lesson-04-task-01.py:71(<listcomp>)
#         1    2.935    2.935    2.935    2.935 lesson-04-task-01.py:21(find_min12_v2)

# cProfile.run('main(find_min12_v3, 10000000)')
#         1    0.000    0.000   27.738   27.738 lesson-04-task-01.py:76(mainP)
#         1    3.662    3.662   27.032   27.032 lesson-04-task-01.py:80(<listcomp>)
#         1    0.000    0.000    0.706    0.706 lesson-04-task-01.py:37(find_min12_v3)

# timeit find_min12_v1 main
def main_time_v1(n):
    SIZE = n
    LOW_VAL = 0
    HGH_VAL = n*100
    massiv = [randint(LOW_VAL, HGH_VAL) for _ in range(SIZE)]

    find_min12_v1(massiv)

# python -m timeit -n 10 -s "import less4task1" "less4task1.main_time_v1(10000)"
# 10 loops, best of 5: 20.2 msec per loop
# python -m timeit -n 10 -s "import less4task1" "less4task1.main_time_v1(100000)"
# 10 loops, best of 5: 219 msec per loop
# python -m timeit -n 10 -s "import less4task1" "less4task1.main_time_v1(1000000)"
# 10 loops, best of 5: 2.15 sec per loop
# python -m timeit -n 10 -s "import less4task1" "less4task1.main_time_v1(5000000)"
# 10 loops, best of 5: 10.4 sec per loop

# timeit find_min12_v2 main
def main_time_v2(n):
    SIZE = n
    LOW_VAL = 0
    HGH_VAL = n*100
    massiv = [randint(LOW_VAL, HGH_VAL) for _ in range(SIZE)]

    find_min12_v2(massiv)
# python -m timeit -n 10 -s "import less4task1" "less4task1.main_time_v2(10000)"
# 10 loops, best of 5: 20.3 msec per loop
# python -m timeit -n 10 -s "import less4task1" "less4task1.main_time_v2(100000)"
# 10 loops, best of 5: 220 msec per loop
# python -m timeit -n 10 -s "import less4task1" "less4task1.main_time_v2(1000000)"
# 10 loops, best of 5: 2.15 sec per loop
# python -m timeit -n 10 -s "import less4task1" "less4task1.main_time_v2(5000000)"
# 10 loops, best of 5: 10.4 sec per loop

# timeit find_min12_v3 main
def main_time_v3(n):
    SIZE = n
    LOW_VAL = 0
    HGH_VAL = n*100
    massiv = [randint(LOW_VAL, HGH_VAL) for _ in range(SIZE)]

    find_min12_v3(massiv)
# python -m timeit -n 10 -s "import less4task1" "less4task1.main_time_v3(10000)"
# 10 loops, best of 5: 18.3 msec per loop
# python -m timeit -n 10 -s "import less4task1" "less4task1.main_time_v3(100000)"
# 10 loops, best of 5: 200 msec per loop
# python -m timeit -n 10 -s "import less4task1" "less4task1.main_time_v3(1000000)"
# 10 loops, best of 5: 1.95 sec per loop
# python -m timeit -n 10 -s "import less4task1" "less4task1.main_time_v3(5000000)"
# 10 loops, best of 5: 9.38 sec per loop


# Вывод
#
# Было протестировано три алгоритма:
# v1 - мой
# v2 - преподавателя
# v3 - реализация стандартными средствами Пайтона
#
# Для алгоритма v1 профилирование на массиве объемом 10.000.000 элементов показало исполнение за 2.738 секунды
# (остальное время заняла генерация массива)
# Для алгоритма v1 профилирование на массиве объемом 10.000.000 элементов показало исполнение за 2.935 секунды
# (остальное время заняла генерация массива)
# Для алгоритма v1 профилирование на массиве объемом 10.000.000 элементов показало исполнение за 0.706 секунды
# (остальное время заняла генерация массива)
#
# На основе профилирования безусловным лидером оказался алгоритм стандартными средствами Пайтона
# (видимо, для поиска минимального элемента массива там используется что-то охрененно кешируемое)
# Алгоритм v1 отрабатывает лучше v2 из-за меньшего количества операций сравнения
# (к тому же в v2 ошибка: первым объявляется второй по минимальности элемент)
# (из-за этого в тестовой функции пришлось применить сравнение множеств, а не кортежей)

# Тайминг проводился в 10 циклов с объемами в 10.000, 100.000, 1.000.000 и 5.000.000 элементов
# Для алгоритма v1 получены значения: 20.2ms, 219ms, 2.15s, 10.4s
# которые хорошо ложатся на линейную зависимость.

# Для алгоритма v2 получены значения: 20.3ms, 220ms, 2.15s, 10.4s
# которые хорошо ложатся на линейную зависимость.

# Для алгоритма v3 получены значения: 18.3ms, 200ms, 1.95s, 9.38s
# которые хорошо ложатся на линейную зависимость.

# Алгоритмы v1 и v2 выходят на одинаковое время обработки при объеме данных больше 1.000.000 элементов
# Но даже на объеме в 5.000.000 элементов алгоритм стандартными средствами Пайтона показывает лучший результат.
# При этом стабильно сохраняется разница в расхождении. На объеме в 1.000.000 она составляла 2.15s-1.95s=0.2s
# На объеме в 5.000.000 10.4s-9.38s=1.02s <=> 0.2s*5 = 1s