# Анонимные, lambda-функции

# # def calk1(a,b):
# #   return a+b
# def calk2(a,b):
#   return a*b
# def calk3(a,b):
#   return a/b
# def math(op,a,b):
#   print(op(a,b))
  
# # calk1=lambda a,b: a+b
# # # a=calk1
# # # print(a(25,5))
# # math(calk1,5,5)

# math(lambda a,b:a+b,5,5)

######################################################################################
# 1.  В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар 
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

#1. без использования лямбда
# spis = [1,2,3, 5, 8, 15, 23, 38]
# res=list()
# for a in spis:
#   if a%2==0:
#     res.append((a,a*a))
# print (res)

# #2. с использования лямбда
# def select(f, col):
#   return [f(x) for x in col]

# def where (f,col):
#   return [x for x in col if f(x)]

# spis = [1,2,3, 5, 8, 15, 23, 38]
# res = select(int, spis)
# print(res)
# res = where(lambda x: x%2 ==0, res)
# print(res)
# res = select(lambda x: (x,x**2), res)

##############################################################
# Функция map

# Функция  map()  применяет  указанную  функцию  к  каждому  элементу  итерируемого  объекта  и 
# возвращает итератор с новыми объектами.

# spis = [x for x in range(1,20)]
# print(spis) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# spis_1 = list(map(lambda x: x+10, spis))
# print(spis_1)  #[11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

# # # Задача 1:Cклавиатурывводитсянекийнаборчисел,вкачестверазделителя
# # # используетсяпробел.Этотнаборчиселбудетсчитанвкачествестроки.Как
# # # превратить list строк в list чисел?
# # # 1.Маленькоеотступление,функциястрока.split()-убираетвсепробелыисоздаем
# # # список из значений строки, пример:
# data = '1 2 3 5 8 15 23 38'
# print(data.split()) # ['1', '2', '3', '5', '8', '15', '23', '38']
# data2=list(map(int, data.split()))
# print(data2) #[1, 2, 3, 5, 8, 15, 23, 38]

# ######
# def where (f,col):
#   return [x for x in col if f(x)]
# spis = [1,2,3, 5, 8, 15, 23, 38]
# res = list(map(int, spis))    
# print(res)                              #[1, 2, 3, 5, 8, 15, 23, 38]
# res = where(lambda x: x%2 ==0, res)
# print(res)                              #[2, 8, 38]
# res = list( map(lambda x: (x,x**2), res))
# print(res)                              #[(2, 4), (8, 64), (38, 1444)]

# ##############################################################
# # Функция filter(f(x),[])

# Функцияfilter()применяетуказаннуюфункциюккаждомуэлементу
# итерируемогообъектаивозвращаетитераторстемиобъектами,длякоторых
# функция вернула True.
# ###### УПРОЩЕНИЕ ПРЕДЫДУЩЕЙПРОГРАММЫ С ИСПОЛЬЗОВАНИЕМ MAP И FILTER
# spis = [1,2,3, 5, 8, 15, 23, 38]
# res = list(map(int, spis))    
# print(res)                              #[1, 2, 3, 5, 8, 15, 23, 38]
# res = filter(lambda x: x%2 ==0, res)
# print(res)                              #[2, 8, 38]
# res = list( map(lambda x: (x,x**2), res))
# print(res)                              #[(2, 4), (8, 64), (38, 1444)]


# data = [x for x in range(10)]
# res = list(filter(lambda x: x % 2 == 0, data))
# print(res) # [0, 2, 4, 6, 8]

# # Как можно сделать этот код лучше, используяfilter()?
# # 💡filter() позволит избавиться от функции where, которую мы писали ранее
# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

# ##############################################################
# # Функция zip(x[],y[])
# Функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами из элементов входных  данных
# На выходе получаем набор данных, состоящий из элементов соответствующих исходному набору.
# Пример:
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14),('user5', 7)]

# # Функция zip () пробегает по минимальному входящему набору:
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]

# ##############################################################
# # Функция enumerate()
  # Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор с кортежами 
  # из индекса и элементов входных данных.
# # Функция enumerate() позволяет пронумеровать набор данных.
# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]


###########################################################################################################################################
#                                                 Файлы
# Файлы в текстовом формате используются для:
# ●Хранения данных
# ●Передачи данных в клиент-серверных проектах
# ●Хранения конфигов
# ●Логирования действий

# Что нужно для работы с файлами:
# 1.Завести переменную, которая будет связана с этим текстовым файлом.
# 2.Указать путь к файлу.
# 3.Указать, в каком режиме мы будем работать с файлом.

# Варианты режима (мод):
# 1.   a– открытие для добавления данных.
# ○ Позволяет дописывать что-то в имеющийся файл.
# ○ Если вы попробуете дописать что-то в несуществующий файл, то файл будет создан и в него начнётся запись.

# 2.    r– открытие для чтения данных.
# ○ Позволяет читать данные из файла.
# ○ Если вы попробуете считать данные из файла, которого не существует, программа выдаст ошибку.

# 3.    w– открытие для записи данных.
# ○ Позволяет записывать данные и создавать файл, если его не существует.

# Миксованные режимы:
# 4.w+
# ○ Позволяет открывать файл для записи и читать из него.
# ○ Если файла не существует, он будет создан.
# 5.r+
# ○ Позволяет открывать файл для чтения и дописывать в него.
# ○ Если файла не существует, программа выдаст ошибку.

# Примеры использования различных режимов в коде:
# 1.Режим a
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()

# ●data.close() — используется для закрытия файла, чтобы разорвать
# подключение файловой переменной с файлом на диске.

# # Ещё один способ записи данных в файл:
# colors = ['red', 'green', 'blue']
# with open('file.txt', 'w') as data:
#   data.write(f'{colors}\n') # ['red', 'green', 'blue'] опостроф \n означает переход на новую строку
#   data.write('line 2\n')    # line 2

# 2.Режим r  - Чтение данных из файла:
path = 'file.txt'
data = open('file.txt', 'r')
for line in data:
  print(line)
data.close()

