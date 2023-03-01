# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются 
# в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов 1-го множества. 
# m - кол-во элементов 2-го множества.

first = [int(x) for x in input().split()]
n = first[0]
m = first[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in input().split()]
k = set(a)
for i in k:
    set_1.add(i)
b = [int(x) for x in input().split()]
k_1 = set(b)
for i in k_1:
    set_2.add(i)
pot = set_1 & set_2
rot = list(pot)
rot.sort()
for i in rot:
    print(i, end= ' ')