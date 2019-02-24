# 9. Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

# тема все-таки функции и рекурсии
# а задания пока без функций и без рекурсии


def summa_cifr(chislo):
     return chislo%10 + ( summa_cifr(chislo//10) if chislo//10 else 0 )
# да я фанат записать решение в одну строку

print("Вводите числа, пока не введете ноль")
isNull = True

# если не хотим считать рекурсию два раза, приходится вводить переменную для хранения
summa_prev = 0

while isNull:
    numC = int(input("число - "))
    if numC == 0: isNull = False
# break это какой-то неуютный выход
    else:
        summa = summa_cifr(numC)
        if summa > summa_prev:
            summa_prev = summa
            chislo = numC

print("Наибольшая сумма цифр =",summa_prev,"у числа",chislo)