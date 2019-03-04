from math import log
import cProfile

# подготовим список необходимой длины из натуральных чисел
def list_n(n):

    # 0 и 1 не простые числа, поэтому сразу поместим на их позиции 0
    a = [0, 0]

    if n <= 21:
        m = n**2
    else:
    # максимальное количество натуральных, среди которых найдется n простых
        m = int(n*(log(n) + log(log(n)))) + 1
    # верно, при n > 20


    for _ in range(2, m):
        a.append(1)

    return a


# Просиди сделать просеивание отдельно. Делаю.
# В результате вернем массив простых чисел с индексацией от 1
def proso(a):
    b = [0]
    for i in range(2, len(a)):
        if a[i] != 0:
            b.append(i)
            j = i + i
            while j < len(a):
                a[j] = 0
                j = j + i

    return b

def eratosfen(n):

    chisla = list_n(n)
    prostye_chisla = proso(chisla)

    return prostye_chisla[n]


def divided_meth(n):

    chisla = list_n(n)
    b = [0]
    for i in range(2, len(chisla)):
        j = 2
        ost = True
        while j*j <= i:
            if i % j == 0:
                ost = False
                break;
            j += 1
        if ost: b.append(i)

    return b[n]


def test_func(func, n):
    test_rslt=[0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]

    if test_rslt[n] == func(n): print("Test OK")
    else: print("Test FALSE")


test_func(eratosfen, 13)
test_func(divided_meth, 13)


#cProfile.run('eratosfen(10000)')
#         1    0.000    0.000    0.174    0.174 less4task2.py:38(eratosfen)
#         1    0.106    0.106    0.132    0.132 less4task2.py:26(proso)
#         1    0.029    0.029    0.042    0.042 less4task2.py:5(list_n)


#cProfile.run('divided_meth(10000)')
#         1    0.690    0.690    0.718    0.718 less4task2.py:46(divided_meth)
#         1    0.020    0.020    0.027    0.027 less4task2.py:5(list_n)

# python -m timeit -n 10 -s "import less4task2" "less4task2.eratosfen(1000)"
# 10 loops, best of 5: 7.35 msec per loop
# python -m timeit -n 10 -s "import less4task2" "less4task2.eratosfen(10000)"
# 10 loops, best of 5: 103 msec per loop
# python -m timeit -n 10 -s "import less4task2" "less4task2.eratosfen(100000)"
# 10 loops, best of 5: 1.43 sec per loop

# python -m timeit -n 10 -s "import less4task2" "less4task2.divided_meth(100)"
# 10 loops, best of 5: 653 usec per loop
# python -m timeit -n 10 -s "import less4task2" "less4task2.divided_meth(1000)"
# 10 loops, best of 5: 21.3 msec per loop
# python -m timeit -n 10 -s "import less4task2" "less4task2.divided_meth(10000)"
# 10 loops, best of 5: 687 msec per loop

# Вывод
# сравнивали два алгоритма нахождения н-го простого числа: решетом эратосфена и методом
# делителей:
# оба показали нелинейную зависимость от входных данных (степенную). На ранних участках кривой:
# Решето Эратосфена, как 10**x = 15 => x = lg(15)
# Метод делителей, как 10**x = 30 => x = lg(30)

