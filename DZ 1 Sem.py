#Задание № 1
#Найдите сумму цифр трехзначного числа.
#Пример:
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)

# number = int (input('Введите 3х значное число: '))
# number_1 = number % 10
# number = number // 10
# number_2 = number % 10
# number = number // 10
# number_3 = number
#
# sum_numbers = number_1 + number_2 + number_3
#
# print(f'Сумма цифр введенного трехзначного числа = {sum_numbers} ({number_3} + {number_2} + {number_1})')





# Задание № 2
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# zuravliki = int(input('Введите количество сделанных журавликов (четное число): '))
# if zuravliki % 2 == 0:
#     del_rovno = zuravliki // 3 #Делим журавликов поровну между Петей, Катей и Сережей
#     Kate = del_rovno * 2
#     Petr = del_rovno // 2
#     Cergey = del_rovno // 2
#     print(f'Всего собрали {zuravliki} журавликов. Из них Петя собрал {Petr}, Катя собрала {Kate}, Сережа собрал {Cergey} жураликов')
# else:
#     print('Введено нечетное число, пожалуйста введите четное')



# Задание № 3
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

# bilet_number = int (input('Введите номер билета (6ти значный): '))
# figure_1 = bilet_number // 100000
# figure_2 = bilet_number // 10000 % 10
# figure_3 = bilet_number // 1000 % 10
# figure_4 = bilet_number // 100 % 10
# figure_5 = bilet_number // 10 % 10
# figure_6 = bilet_number % 10
# if figure_1 + figure_2 + figure_3 == figure_4 + figure_5 + figure_6 and bilet_number // 1000000 == 0 and bilet_number // 100000 != 0:
#     print('Билет счастливый')
# else:
#     print('Билет несчастливый или введено неверно')



