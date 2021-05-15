'''
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном
списке. Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
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
for item in original_list:
    if original_list.count(item) == 1:
        new_list.append(item)

print(new_list)
