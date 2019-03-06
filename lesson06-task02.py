# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

import array
from collections import namedtuple

# если нужно было именно сложение в столбик, то так и надо было ставить задачу.
# а это решение без использования int() и hex() - как и было указано в ТЗ
my_int = [i for i in range(16)]
my_hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
# словарь для перевода туда-сюда
dict_pretty = dict(zip(my_hex, my_int))
# словарь для перевода сюда-обратно
dict_betty = dict(zip(my_int, my_hex))


# возвращаем десятичное
# хотя и можно было сразу шестнадцатеричное число вернуть
def calc_int(number):
    ret_num = 0
    for i, item in enumerate(reversed(number), 0):
        ret_num += dict_pretty[item] * 10 ** i

    return ret_num


# переводим в шестнадцатеричное, чтобы сделать хоть что-то
def calc_out(int_num):
    # опять массив
    number = array.array('u')
    while int_num // 16 != 0:
        number.append(dict_betty[int_num % 16])
        int_num //= 16
    number.append(dict_betty[int_num % 16])

    # а возвращаем список - у него вывод красивый :)
    return number.tolist()[::-1]


# даже с массивом, хотя в будущем тип 'u' и будет исключен
number1 = array.array('u', [x for x in input("Введите число 1: ")])
number2 = array.array('u', [x for x in input("Введите число 2: ")])

itog = namedtuple('Itog', 'val1 val2')
itog.val1 = calc_int(number1)
itog.val2 = calc_int(number2)

print("sum     ", calc_out(itog.val1 + itog.val2))
print("multiply", calc_out(itog.val1 * itog.val2))
