# Задача №1. Решение в группах Последовательностью Фибоначчи называется последовательность чисел 
# a0 , a1 , ..., an , ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). 
# Требуется найти N-е число Фибоначчи Input: 7 Output: 21 
# Задание необходимо решать через рекурсию

# # 0, 1, 1, 2, 3, 5, 8, 13, 21
# def fibonachi (n):
#   if n==0 or n==1:
#     return 1
#   return fibonachi(n-1)+fibonachi(n-2)

# fi=int(input("Введите число: "))
# print(f"Последовательность фибоначи: {fibonachi(fi-2)} ")      #Ответ 8
       
 ########################################################################  
#  Задача №2. Решение в группах Хакер Василий получил доступ к классному журналу и хочет заменить все свои
#  минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, 
#  но наоборот: все максимальные – на минимальные. 
# Input: 5 -> 1 3 3 3 4 
# Output: 1 3 3 3 1  

# # Мой вариант
# n = int(input("Введите количество оценок Василия:"))
# OcVas=[]
# for i in range(n):
#   OcVas.append(int(input(f"Введите {i+1} оценку Василия в журнале: ")))
# maxOc=OcVas[0]; minOC=OcVas[0]
# print(f"Оценки Васи в журнале: {OcVas}")  
# # for i in range(len(OcVas)):
# #   if maxOc<OcVas[i]:
# #     maxOc=OcVas[i]
# #   elif minOC>OcVas[i]:
# #     minOC=OcVas[i]
# maxOc=max(OcVas); minOC=min(OcVas)
# for i in range(len(OcVas)):
#   if OcVas[i]== maxOc:
#     OcVas[i]=minOC    
# print(f"Оценки Васи в журнале после махинаций: {OcVas}")  

# Вариант препода
# n=int(input("input :"))
# list1=[]
# for i in range(n):
#   x=int(input())
#   list.append(x)
# max_n = max(list1)
# min_n = min(list1)
# for i in range(len(list1)):
#   if list1[i]==max_n:
#     list1[i]=min_n
# print(list1)

 ########################################################################  
 
#  Задача No3. Решение в группах
# Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое 
# имеет 2 делителя: 1  и n(само число)
# Input: 5
# Output: yes 

# # # Мой вариант
# def ProstN(n):
#   koldel=0
#   for i in range(1,n):
#     if n%i==0:
#       koldel+=1
#   return koldel
# n = int(input("Введите число для проверки является ли он простым: "))
# if ProstN(n)<=2:
#   print(f"Ваше число {n} является простым")
# else:
#   print(f"Ваше число {n} не является простым")

# # Вариант препода
# def prime(n):
#   flag=True
#   i=2
#   while i < n and flag:
#     if n % i == 0:
#       flag=False
#     i+=1
#     if flag:
#       return 'yes'
#     else:
#       return 'no'
# n = int(input("Input N:"))
# print(prime(n))

######################################################################################

# Задача No4. Решение в группах
# Дано натуральное число N и 
# последовательность из N элементов. 
# Требуется вывести эту последовательность в 
# обратном порядке.
# Примечание. В программе запрещается 
# объявлять массивы и использовать циклы 
# (даже для ввода и вывода).
# Input:    2 -> 3 4
# Output: 4 3

def f(n):
  if n==0:
    return ''
  else:
    k = input("Input numbers: ")
    return f(n-1) + f" {k}"
n = int(input("Input kol. num: "))
print (f(n))