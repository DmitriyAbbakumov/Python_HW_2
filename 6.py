# Задача 5 - HARD необязательная

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в N-мерном пространстве. 
# Сначала задается N с клавиатуры, потом задаются координаты точек.

N = int(input("Введите N-мерность пространства: "))
lst = []
S = 0

for i in range(N):
    lst.append(int(input(f'Введите коодинату точки "A" на {i+1} оси: ')))
    lst.append(int(input(f'Введите коодинату точки "B" на {i+1} оси: ')))
    S = S + (lst[-1] - lst[-2])**2
print(f'Вы ввели координаты точки "A": {[lst[i] for i in range(len(lst)) if i%2==0]}')
print(f'Вы ввели координаты точки "B": {[lst[i] for i in range(len(lst)) if i%2!=0]}')
print(f'Расстояние между точками "A" и "B" {S**0.5}')