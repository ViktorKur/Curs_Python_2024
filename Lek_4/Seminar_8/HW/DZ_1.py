# Задание1.Сумма чисел Во входном файле numbers.txt записано N целыхч исел, 
# которые могут быть разделены пробелами и концами строк. Напишите программу,которая выводит сумму чисел 
# во выходной файл answer.txt. 
# Пример: 
# Содержимое файла numbers.txt 
#   2 
# 2 
#  2 
#      2  
# Содержимоефайла answer.txt 8
# Мой вариант
import os
with open('numbers.txt','r',encoding='utf-8') as f: 
    num_file = f.readlines()
num = [int(n) for n in num_file if n]
suma = sum(num)
with open('answer.txt','w',encoding='utf-8') as f: 
    f.write(str(suma))
# print(num)
# print(suma)


# # Эталонноерешение: 
# import os 
# #Открываемвходнойфайлдлячтения 
# # os.chdir('D:\Education_GEEK_BRAIN\Seminar_Folder\Python_projects 2024\Lek_4\Seminar_8\HW')
# numbers_file = open("numbers.txt", "r", encoding = "utf-8") 
# print(numbers_file)
# #Инициализируемпеременнуюдляхранениясуммычисел 
# total_sum=0 
# #Читаемфайлпострочно 
# for line in numbers_file: 
# #Разбиваемстрокуначасти,используяпробелыиновыестрокив качестверазделителей 
# #Преобразуемкаждуючастьвцелоечислоинакапливаемсумму 
#   numbers=[int(num) for num in line.split() if num] 
#   total_sum+=sum(numbers)
# #Закрываемфайлпослечтения 
# numbers_file.close() 
# #Открываемвыходнойфайлдлязаписи 
# sum_file=open("answer.txt","w",encoding="utf-8")
# #Записываемсуммуввыходнойфайл 
# sum_file.write(str(total_sum))
# # Закрываем выходной файл 
# sum_file.close()