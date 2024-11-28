# Задание 2. Сумма чисел В файле zen.txt хранится так называемый Дзен Пайтона — 
# текст философии программирования на языке Python. Выглядит он так: 
  # Beautiful is better than ugly. 
  # Explicit is better than implicit. 
  # Simple is better than complex. 
  # Complex is better than complicated. 
  # Flat is better than nested.
  # Sparse is better than dense.
  # Readability counts. 
  # Special cases aren't special enough to break the rules.
  # Although practicality beats purity.
  # Errors should never pass silently. 
  # Unless explicitly silenced. 
  # In the face of ambiguity, refuse the temptation to guess.
  # There should be one-- and preferably only one--obvious way to do it.
  # Although that way may not be obvious at first unless you're Dutch.
  # Now is better than never.
  # Although never is often better than *right* now.
  # If the implementation is hard to explain, it's a bad idea. 
  # If the implementation is easy to explain, it may be a good idea. 
  # Namespaces are one honking great idea-- let's do more of those!

#   Напишите программу, которая выводит на экран все строки этого файла в обратном порядке. 
#   Кстати, попробуйте открыть консоль Python и ввести команду import this. 
#   Результат работы программы:
#   Namespaces are one honking great idea-- let's do more of those! 
#   If the implementation is easy to explain, it may be a good idea.
#   If the implementation is hard to explain, it's a bad idea. 
#   Although never is often better than *right* now.

# Мой вариант
# import os
# os.chdir('D:\Education_GEEK_BRAIN\Seminar_Folder\Python_projects 2024\Lek_4\Seminar_8\HW')
# with open('zen.txt', 'r', encoding='utf-8') as file:
#   txt = file.readlines()
#   res_txt = [txt[i] for i in range(len(txt)-1, -1, -1)]
#   print(*res_txt)
  
#Эталонное решение: 
import os
# Открываем файл для чтения 
os.chdir('D:\Education_GEEK_BRAIN\Seminar_Folder\Python_projects 2024\Lek_4\Seminar_8\HW')
philosophical_text = open("zen.txt", "r")
# Считываем все строки в список 
lines = philosophical_text.readlines() 
# Закрываем файл после чтения 
philosophical_text.close() 
# Проходим по строкам в обратном порядке и выводим каждую строку без символа новой строки в конце 
for line in reversed(lines): 
  print(line.strip())