# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.

# функция
def primfacs(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(int(i))
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(n)
    return primfac


LOW_VAL = 2
HGH_VAL = 14399

LOW_DIV = 2
HGH_DIV = 9

all_div = 0
cnt = []

for i in range(LOW_VAL, HGH_VAL+1):
    for j in range(LOW_DIV, HGH_DIV+1):
        all_div += i % j
#        print(i, "%", j, "=", i % j, sep='', end='  ')
    if not all_div: cnt.append(i)
#    print(" ", all_div)
    all_div = 0
# 8,9,5,7
print("всего ", len(cnt))
print(cnt)
print(primfacs(cnt[0]))
print(primfacs(2*3*4*5*6*7*8*9))


