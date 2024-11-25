# Задание 1. Новые списки
# Даны три списка:
# 1. floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
# 2. names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
# 3. numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
# Напишите код, который создаёт три новых списка. Вот их содержимое:
# 1. Каждое число из списка floats возводится в третью степень и округляется
# до трёх знаков после запятой.
# 2. Из списка names берутся только имена минимум из пяти букв.
# # 3. Из списка numbers берётся произведение всех чисел
# from functools import reduce
# Мой вариант
# floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
# names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
# numbers = [22, 33, 10, 6894, 11, 2, 1]
# resFlt = [float(round(i**3,3)) for i in floats]
# resFlt = list(map(lambda x: round(x ** 3, 3), floats))
# resname=[n for n in names if len(n)>=5]
# resname = list(filter(lambda name: len(name) >= 5, names))
# resnumb = reduce(lambda num, num2: num*num2, numbers)
# print (resFlt)
# print (resname)
# print (resnumb)

#Эталонный вариант
from functools import reduce
# Исходные списки
floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers = [22, 33, 10, 6894, 11, 2, 1]
# Применяем функцию map для возведения в третью степень и округлениядо трех знаков после запятой
map_result = list(map(lambda x: round(x ** 3, 3), floats))
# Применяем функцию filter для выбора имен из пяти и более букв
filter_result = list(filter(lambda name: len(name) >= 5, names))
# Применяем функцию reduce для нахождения произведения всех чисел всписке
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers)
# Вывод результатов
print(map_result)
print(filter_result)
print(reduce_result)