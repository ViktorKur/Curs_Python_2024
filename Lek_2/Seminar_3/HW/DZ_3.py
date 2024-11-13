# Задача 3. Сортировка
# Дан список из N чисел. Напишите программу, которая сортирует элементы
# списка по возрастанию и выводит их на экран. Дополнительный список
# использовать нельзя.
# Также нельзя использовать готовые функции sorted/min/max и метод sort
# Постарайтесь придумать и написать как можно более эффективный алгоритм
# сортировки.
# Пример:
# Изначальный список: [1, 4, –3, 0, 10]
# Отсортированный список: [–3, 0, 1, 4, 10]

# Мой вариант 
SpisN = [1, 4, -3, 0, 10, -1, -40, 30]
print(f"      Исходные данные: {SpisN}")
for i in range(0, len(SpisN)-1):
  minN = SpisN[0]
  minIndx = 0
  # print(SpisN)
  for j in range(1,len(SpisN)):
    if SpisN[j]<SpisN[j-1]:
      minN=SpisN[j]
      SpisN[j]=SpisN[j-1]
      SpisN[j-1]=minN
print(f"Отсортированые данные: {SpisN}")    

# # Эталонное решение:
# # Исходный список чисел
# original_list = [1, 4, -3, 0, 10]
# # Вывод исходного списка
# print('Изначальный список: ', original_list)
# # Реализация сортировки пузырьком (Bubble Sort)
# for i in range(len(original_list) - 1):
# # Проход по всем элементам списка, за исключением уже отсортированных
#   for j in range(len(original_list) - 1 - i):
# # Сравнение текущего элемента с следующим
#      if original_list[j] > original_list[j + 1]:
# # Если текущий элемент больше следующего, меняем их местами
#        original_list[j], original_list[j + 1] = original_list[j + 1], original_list[j]
# # Вывод отсортированного списка
# print('Отсортированный список: ', original_list)