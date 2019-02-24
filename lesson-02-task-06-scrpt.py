
# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше
# введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.

from random import random

LOW_VAL=0
HGH_VAL=100
MAX_ATTEMPT=10

attempts = 0

answer = int(LOW_VAL + (HGH_VAL - LOW_VAL + 1)*random())

while attempts < MAX_ATTEMPT:
    print("Ваша попытка #",attempts+1)
    rand = int(input("Угадайте число: "))
    print("Ваш ответ:", end=' ')
    if rand < answer: print("меньше", end=' ')
    elif rand > answer: print("больше", end=' ')
    else: break
    
    print("загаданного числа")
    attempts += 1

if attempts < MAX_ATTEMPT: print("ПРАВИЛЬНЫЙ !!! ")
#else: print("Попытки закончились\nЗагаданное число было:",answer)
else: print("Попытки закончились :(")

print("Было загадано число:",answer)