from logger import input_data, print_data
def interface():
  print('Добрый день! вы попали на спец бот справочник от ГикБрейнсэ \n 1- запись данных \n 2 - вывод данных')
  command =int(input("Введите число: "))
  while command!=1 and command!=2 and type(command)!=int:
    print ("Неправильный ввод")
    command =int(input("Введите число: "))
  # return command
  if command == 1:
    input_data()
  elif command==2:
    print_data()

 
  