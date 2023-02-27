# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значен


import random

N = int(input('Введите длину списка: '))
X = int(input('Введите искомое число: '))
min = 0
List = []
count = 0
for i in range(N):
    K = random.randint(1, 100)
    List.append(K)
print(List)
max = List[0]
for i in range(len(List)):
    if X == List[i]:
        count += 1
print(f'Число встречается {count} раз')
if count == 0:
    for i in range(len(List)):
        max_2 = List[i]
        if X >= List[i] and List[i] > min:
            min = List[i]
        elif max > X and max > List[i]:
            max = List[i]
if max - X > X - min:
    print(f'Максимально близкое значение к введенному числу = {min}')
else:
    print(f'Максимально близкое значение к введенному числу = {max}')

