'''
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
 должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает
  за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''

from math import factorial

while True:
    try:
        n = int(input('Факториал скольки чисел вы хотите посчитать? '))
        break
    except ValueError:
        print('ValueError - то, что вы ввели не является числом. Повторите ввод')


def fact(number):
    for i in range(number):
        yield factorial(i + 1)


for item in fact(n):
    print(item)
