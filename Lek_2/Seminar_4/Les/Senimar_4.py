# Задача №1. Решение в группах Напишите программу, которая принимает на вход строку, и отслеживает, 
# сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n. 
# Input: a a a b c a a d c d d 
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2 
# Для решения данной задачи используйте функцию .split()
# Stroka = input("Введите буквы через пробел: ").split()
# res = {}
# for i in Stroka:
#   if i in res:
#     print (f"{i}_{res[i]}", end = " ")
#   else:
#     print(i, end = " ")
#   res[i] = res.get(i,0)+1
#   print(res)

  #############################################################################
  
  
# Задача №2. Решение в группах Пользователь вводит текст(строка). 
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. Определите, сколько различных 
# слов содержится в этом тексте. 
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells 
# I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13
# моя версия
# wrd = set(input("Введите текст: ").split())
# wrd = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# count=0
# wrd=wrd.lower()
# wrd = set(wrd.split())
# for i in wrd:
#   count+=1
# # print(wrd)  
# print(f"Количество слов в вашем тексте = {count}")

# #Эталонная
# stroka = input().split()
# set_1 = set()
# for i in stroka:
#   set_1.add(i.lower())
# print(len(set_1))
  
#   ########################################################################################################
  
#  Задача3 Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
#    “Задана последовательность неотрицательных целых чисел. Требуется определить
#    значение наибольшего элемента последовательности, которая завершается первым 
#    встретившимся нулем (число 0 не входит в последовательность)”. Однако 2  друга
#    оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание. 
#    Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи
#    обратились к Вам, студентам. Примечание: Программные коды на следующих слайдах

# #  Ваня: 
# n = int( input()) 
# max_number = 1000 
# while n != 0:  
#   n = int( input())
#   if max_number > n: 
#     max_number = n 
# print (max_number) 
      
# # Петя: 
# # n = int( input ()) 
# # max_number = -1 
# # while n < 0:   
# #   n = int( input ()) 
# #   if max_number < n:       
# #     n = max_number 
# # print (n) 
    
#     # Мой вариант
# maxN=0
# n=1
# while n>0:
#   n=int(input("Введите положительное и большее нуля число n, для окончания ввода введите 0 :"))
#   if n>maxN:
#     maxN=n
# print(f"Max N={maxN} ") 

# Эталонное решение
n=int(input("N= ")) 
max_number = -1 
while n != 0:   
  n = int( input ("N= ")) 
  if max_number < n:       
    max_number = n
print (max_number) 