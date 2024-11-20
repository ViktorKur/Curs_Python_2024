# Задача 2. Случайные соревнования
# Мы хотим протестировать работу электронной таблицы для участников
# некоторых соревнований. Есть два списка, то есть две команды, по 20
# участников в каждом. В них хранятся очки каждого участника — вещественные
# числа с двумя знаками после точки, например 4.03.
# Член одной команды соревнуется с участником другой команды под таким же
# номером. То есть первый соревнуется с первым, второй — со вторым и так
# далее.
# Напишите программу, которая генерирует два списка участников (по 20
# элементов) из случайных вещественных чисел (от 5 до 10). Для этого найдите
# подходящую функцию из модуля random. Затем сгенерируйте третий список, в
# котором окажутся только победители из каждой пары.
# Пример:
# Первая команда: [7.86, 6.76, 9.97, 9.08, 5.45, 6.9, 8.65, 5.17, 8.17, 5.06, 7.56, 7.1,
# 7.18, 8.25, 5.53, 7.95, 8.91, 7.11, 8.29, 9.52]
# Вторая команда: [7.13, 5.7, 8.89, 5.36, 5.62, 9.46, 5.82, 8.67, 8.41, 7.0, 5.31, 7.8,
# 9.93, 7.76, 7.4, 8.26, 7.94, 5.71, 7.89, 7.77]
# Победители тура: [7.86, 6.76, 9.97, 9.08, 5.62, 9.46, 8.65, 8.67, 8.41, 7.0, 7.56, 7.8,
# 9.93, 8.25, 7.4, 8.26, 8.91, 7.11, 8.29, 9.52]

# # # # # Мой вариант решения задачи
# import random
# n = int(input("Введите количество участников: "))
# comand1 = [round(random.uniform(5,10),2) for i in range(n)]
# comand2 = [round(random.uniform(5,10),2) for i in range(n)]
# rezComand = []
# for i in range(n):
#   if comand1[i]>comand2[i]:
#     rezComand.append(comand1[i])
#   elif comand2[i]>comand1[i] or comand2[i]==comand1[i] :
#     rezComand.append(comand2[i])
# print(f"1я коанда: {comand1}")
# print(f"2я коанда: {comand2}")
# print(f'Победители тура: {rezComand}')

# # Эталонный вариант
import random
# Генерация первой команды из 20 случайных вещественных чисел в диапазоне от 5 до 10
first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
# Генерация второй команды аналогично первой
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
# Определение победителей тура путем сравнения значений в первой и второй командах
winners = [first_team[i_player] if first_team[i_player] > second_team[i_player]
           else second_team[i_player] for i_player in range(20)]
# Вывод данных
print('Первая команда:', first_team)
print('Вторая команда:', second_team)
print('Победители тура:', winners)