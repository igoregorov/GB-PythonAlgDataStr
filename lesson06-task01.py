# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.


from collections import namedtuple

# Именованный кортеж для хранения данных о предприятии (название, доход за год)
company = namedtuple('Company', 'name revenue')

print("Введите данные придприятий в формате:\n"
      "->название\n"
      "->прибыль за четыре квартала через пробел\n"
      "Для окончания ввода - оставьте название пустым\n")

# храним средний доход за год
avg_company = 0.0

# список предприятий
list_companies = []

while True:
    name = input("Название: ")
    if name == '':
        break
    revenue = sum(float(x) for x in input("Прибыль: ").split(' '))

    # добавляем в среднее годовую прибыль предприятия
    avg_company += revenue

    # добвляем предприятие в список
    list_companies.append(company(name, revenue))

# считаем среднюю прибыль предприятий за год
avg_company /= len(list_companies) if len(list_companies) else 1.0

print("Предприятия с доходом за год меньше среднего:",
      ' '.join(
          [x.name for x in list_companies if x.revenue < avg_company])
      )
print("Предприятия с доходом за год больше среднего:",
      ' '.join(
          [x.name for x in list_companies if x.revenue > avg_company])
      )
