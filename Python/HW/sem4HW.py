#1)Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

num = int(input("До какого числа после запятой вывести число Пи "))

PI = (1/16**0) * (4/(8 * 0 + 1) - 2/(8 * 0 +4) - 1/(8 * 0 + 5) - 1/(8 * 0 + 6))

for k in range(1, num):
    PI += (1/16**k) * (4/(8 * k + 1) - 2/(8 * k +4) - 1/(8 * k + 5) - 1/(8 * k + 6))

print(round(PI, num))

#2)Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите число:  "))
i = 2
while i <= num: 
    if num % i == 0:
        print(i, end = " ")
        num = num/i
        i = 1
    i += 1

#3)Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
arr1=[2,3,4,5,3,234,543,4]
arr2=[]
for i in range(len(arr1)):
    if arr1.count(arr1[i]) == 1: arr2.append(arr1[i])
print(arr2)

#4)Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.


from random import randint as rd

k = int(input())

arr = list()
for i in range (k, 0, -1):
    x = rd(-100,100)
    if x>0 and i!=k:
        arr.append(f'+{x}*x^{i}')
    else:
        arr.append(f'{x}*x^{i}')
x = rd(-100,100)
if x>0 and i!=k:
    arr.append(f'+{x}')
else:
    arr.append(f'{x}')
arr.append(' =0')
print(''.join(arr))