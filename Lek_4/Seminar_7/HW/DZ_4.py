# Задача 4. Уникальный шифр
# Напишите функцию, которая принимает строку и возвращает количество
# уникальных символов в строке. Используйте для выполнения задачи
# lambda-функции и map и/или filter.
# Сделайте так, чтобы алгоритм НЕ был регистрозависим: буквы разного
# регистра должны считаться одинаковыми.
# Пример:
# message = "Today is a beautiful day! The sun is shining and the birds are
# singing."
# unique_count = count_unique_characters(message)
# print("Количество уникальных символов в строке:", unique_count)
# Вывод: количество уникальных символов в строке — 5

def count_unique_characters(stroka):
  low_str = stroka.lower()
  print(low_str)
  unique_chars = list(filter(lambda x: low_str.count(x.lower()) == 1, low_str.lower()))
  print(unique_chars)
  return len(unique_chars)
message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке - ", unique_count)



# # Эталонное решение:
# def count_unique_characters(string):
#   # Приводим строку к нижнему регистру, чтобы сделать подсчет  регистронезависимым
#   lower_string = string.lower()
#   # Используем filter для выбора символов, которые встречаются в  строке ровно один раз
#   unique_chars = list(filter(lambda c: lower_string.count(c.lower()) == 1, lower_string))
#   # Выводим уникальные символы (по желанию, можно удалить эту  строку)
#   print(unique_chars)
#   # Возвращаем количество уникальных символов
#   return len(unique_chars)
# # Пример использования:
# message = "Today is a beautiful day! The sun is shining and the birds are singing."
# unique_count = count_unique_characters(message)
# print("Количество уникальных символов в строке:", unique_count)