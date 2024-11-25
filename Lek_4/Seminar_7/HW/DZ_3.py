# Задача 3. Палиндром
# Используя модуль collections, реализуйте функцию can_be_poly, которая
# принимает на вход строку и проверяет, можно ли получить из неё палиндром.
# Пример кода:
# print(can_be_poly('abcba'))
# print(can_be_poly('abbbc'))
# Результат:
# True 
# False



# Мой вариант решения
# from collections import Counter
# def  can_be_poly (stroka):
#   chast= Counter(stroka)
#   filtr = list(filter(lambda x:x%2!=0,chast.values()))
#   # print(chast)
#   # print(filtr)
#   if len(filtr)<=2:
#     return True 
#   else:
#     return False
# print(can_be_poly('abcba') )   
# print(can_be_poly('abbbc') )



# Эталонный вариант
from collections import Counter
def can_be_poly(val: str) -> bool:
  # Создаем счетчик частот символов в строке
  char_counts = Counter(val)
  # Проверяем количество символов с нечетным количеством вхождений
  odd_count = len(list(filter(lambda x: x % 2, char_counts.values())))
  # Условие для проверки возможности формирования палиндрома
  return odd_count < 2
print(can_be_poly('eerru')) # Ожидаемый результат: True
print(can_be_poly('abbcba')) # Ожидаемый результат: True
print(can_be_poly('abbbc')) # Ожидаемый результат: False