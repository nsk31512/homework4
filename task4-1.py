'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения
расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

from sys import argv


def salary(production, rate, bonus):
    salary = float(production) * float(rate) + float(bonus)
    return salary
    print(f'Зарплата: {salary}')


try:
    script_name, production, rate, bonus = argv
except ValueError:
    print('Value Error - вы ввели мало либо много значений. Если премия не предусмотрена введите 0')
else:
    salary = salary(production, rate, bonus)
    print(f'Зарплата: {salary}')
