# Задача 6 *. Кинотеатр X мальчиков и Y девочек пошли в кинотеатр и купили билеты на идущие подряд места в одном ряду.
# Напишите программу, которая выдаст, как нужно сесть мальчикам и девочкам, чтобы рядом с каждым мальчиком сидела хотя бы 
# одна девочка, а рядом с каждой девочкой — хотя бы один мальчик. На вход подаются два числа: количество мальчиков
# X и количество девочек Y. В ответе выведите какую-нибудь строку, в которой будет ровно X символов B, обозначающих мальчиков, 
# и Y символов G, обозначающих девочек, удовлетворяющую условию задачи. Пробелы между символами выводить не нужно. 
# Если рассадить мальчиков и девочек согласно условию задачи невозможно, выведите строку «Нет решения».

# Мое решение задачи
print("Введите поочереди количество мальчиков и девочек купивших билет")
b=int(input("Введите количество мальчиков: "))
g=int(input("Введите количество девочек: "))
rad1=[]
rad2=[]
if b==g or g==b:
  for i in range (b):
    rad1.append('B')
    rad1.append('G')
    rad2.append('G')
    rad2.append('B')
  print (f"Первый вариант рассадки: {rad1}")
  print (f"Первый вариант рассадки: {rad2}")
elif b>g and b-g==1:
  for i in range (b):
    rad1.append('B')
    rad1.append('G')
  rad1.pop(-1)
  print (f"Первый вариант рассадки: {rad1}")
elif g>b and g-b==1:
  for i in range (g):
    rad2.append('G')
    rad2.append('B')
  rad2.pop(-1)
  print (f"Вариант рассадки в попорядку в ряду кинотеатра: {rad2}")
else :
  print("Нет решения, невозможно рассадить мальчиков и девочек соглвсно условию")
  
  
  #Эталонное решение задачи
  #Ввод количества мальчиков и девочек 
# boys=int(input('Введитекол-вомальчиков:')) 
# girls=int(input('Введитекол-водевочек:')) 
# #Инициализация пустой строки для результата 
# answer='' 
# # #Проверка возможности корректного распределения мальчиков и девочек 
# if(boys>2*girls) or (girls>2*boys): # #Еслимальчиковилидевочекслишкоммногодлякорректного чередования 
# print('Нетрешения') 
# elif boys>=girls: # #Еслимальчиковбольшеилиихколичестворавноколичеству девочек 
# k=boys-girls #Количестволишнихмальчиков 
# #Вставкалишнихмальчиковмеждудевочками 
# for bgb in range(k): 
#   answer+='BGB' 
# #Добавлениеоставшихсямальчиковидевочек 
# for bg in range(girls-k):
#   answer+='BG' else:
# Если девочек больше, чем мальчиков 
# k = girls- boys 
# # Количество лишних девочек 
# # Вставка лишних девочек между мальчиками 
# for gbg in range(k): 
#   answer += 'GBG' 
# # Добавление оставшихся мальчиков и девочек 
# for gb in range(boys- k): 
#   answer += 'GB' 
# # Вывод ответа 
# print(answer)
