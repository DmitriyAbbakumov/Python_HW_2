# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0 
# 2

from random import randint
lst = []
a = int(input("Введите кол-во монет: "))
for i in range(a):
    lst.append(randint(0, 1))
print(f'Вот ваши монеты - {lst}')

count_1 = count_2 = 0
for i in lst:
    if i == 0:
        count_1 +=1
    else:
        count_2 +=1
        
if count_1 < count_2:
    print(f'Минимальное кол-во монет = {count_1}')
else:
    print(f'Минимальное кол-во монет = {count_2}')