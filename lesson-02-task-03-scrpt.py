# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.

print("variant 1")

strN = input("Введите число: ")
revN = ''.join(reversed(strN))
print("Обратное: ", revN)

print("variant 2")
a = int(strN)
new_a = 0

for i in range(0, len(strN)):

# основная идея: брать остаток от деления на 10 (последнюю цифру) и добавлять в новое число.
# новое число каждый раз умножаем на десять. Умножение делаем первым действием.
    new_a *= 10
    new_a += a % 10
    a //= 10
	
print("Обратное-2: ", new_a)

print("variant 3")

# ну и то же самое, в виде функции с подобием рекурсии
def cifra_nao(chislo,new_chislo):
    new_chislo *= 10
    new_chislo = new_chislo + chislo%10
    if chislo > 10: return cifra_nao(chislo//10,new_chislo)
    return new_chislo

print("Обратное - 3:",cifra_nao(int(strN),0))

