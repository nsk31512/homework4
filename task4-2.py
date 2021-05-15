'''
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''
from random import randrange


def generator(count, maximum):
    num = int(randrange(maximum))
    for i in range(count):
        yield num
        num = int(randrange(maximum))


while True:
    try:
        number_of_range = int(input('Сколько элементов в списке вы хотите создать? '))
        maximum_of_range = int(input('Какое максимальное значение в этом списке? '))
        break
    except ValueError:
        print('Value Error - введите целое число')

original_generator = generator(number_of_range, maximum_of_range)
original_list = []
for item in original_generator:
    original_list.append(item)

new_list = []
for i in range(len(original_list)):
    try:
        if original_list[i + 1] > original_list[i]:
            new_list.append(original_list[i + 1])
    except IndexError:
        break
print(new_list)
