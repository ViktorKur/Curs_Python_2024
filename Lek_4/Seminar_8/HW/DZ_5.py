# Задача 5*. «Война и мир» Мало кто не знает знаменитый роман Л. Н. Толстого «Война и мир». 
# Это довольно объёмное произведение лежит в архиве voina-i-mir.zip. 
# Напишите программу, которая подсчитывает статистику по буквам 
# (не только русского алфавита) в этом романе и выводит результат на экран (или в файл).
# Результат должен быть отсортирован по частоте встречаемости букв (по возрастанию или убыванию).
# Регистр символов имеет значение. Архив можно распаковать вручную, но, если хотите, можете изучить 
# документацию по модулю zipfile (можно использовать и другой модуль) и попробовать написать код,
# который будет распаковывать архив за вас.

import os
os.chdir('D:\Education_GEEK_BRAIN\Seminar_Folder\Python_projects 2024\Lek_4\Seminar_8\HW')
with open('voyna-i-mir.txt','r', encoding='utf-8') as fl: 
  txt=fl.read()
  spisKolSimv={} 
for simv in txt: 
  if simv.isalpha(): 
    spisKolSimv[simv] = spisKolSimv.get(simv,0)+1
sorted_simvs = sorted(spisKolSimv.items(), key=lambda x: (-x[1], x[0])) 
with open("statistik.txt", "w", encoding="utf-8") as f: 
  for simv, kolSovp in sorted_simvs: 
    f.write(f"{simv}: {kolSovp}\n")


# # Эталонное решение: 
# import os
# os.chdir('D:\Education_GEEK_BRAIN\Seminar_Folder\Python_projects 2024\Lek_4\Seminar_8\HW')
# import zipfile 
# #Открываем архив и ищем текстовый файл 
# with zipfile.ZipFile("voina-i-mir.zip","r") as zip_ref: 
# #Получаем список файлов в архиве и выбираем первый текстовый файл 
#   file_name=[name for name in zip_ref.namelist() if name.endswith('.txt')][0] 
# #Открываем выбранный файл и читаем его содержимое 
#   with zip_ref.open(file_name) as file: 
#     text=file.read().decode('utf-8') 
# #Инициализируем словарь дляподсчета количества символов 
# char_count={} 
# #Подсчитываем количество вхождений каждого символа 
# for char in text: 
#   if char.isalpha(): 
# #Учитываем только буквы 
#     if char in char_count: 
#       char_count[char]+=1 
#     else:
#       char_count[char] = 1 
# # Сортируем символы по частоте (в убывании) и по алфавиту при равенстве частоты 
# sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0])) 
# # Записываем результаты в файл 
# with open("statistik.txt", "w", encoding="utf-8") as file: 
#   for char, freq in sorted_chars: 
#     file.write(f"{char}: {freq}\n")