# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.


a = input("Первая буква: ")
b = input("Вторая буква: ")

a=ord(a.lower())
b=ord(b.lower())

print("Первая буква стоит на",a-96,"месте")
print("Вторая буква стоит на",b-96,"месте")

d = abs(b - a) - 1 

if  d == 0  : print("Между ними нет букв")
elif d < 0  : print("Это одна и та же буква")
else        : print("Между ними",d,"букв(а)")
