# Задача 5. Пицца
# В базе данных интернет-магазина PizzaTime хранятся сведения о том, кто, что и
# сколько заказывал у них в определённый период. Вам нужно структурировать
# эту информацию и определить, сколько всего пицц купил каждый заказчик.
# На вход в программу подаётся N заказов. Каждый заказ представляет собой
# строку вида «Покупатель — название пиццы — количество заказанных пицц».
# Реализуйте код, который выводит список покупателей и их заказов по алфавиту. 
# Учитывайте, что один человек может заказать одну и ту же пиццу несколько раз.
# Пример
# Введите количество заказов: 6
# Первый заказ: Иванов Пепперони 1
# Второй заказ: Петров Де-Люкс 2
# Третий заказ: Иванов Мясная 3
# Четвёртый заказ: Иванов Мексиканская 2
# Пятый заказ: Иванов Пепперони 2
# Шестой заказ: Петров Интересная 5
# Иванов:
# Мексиканская: 2
# Мясная: 3
# Пепперони: 3
# Петров:
# Де-Люкс: 2
# Интересная: 5

# Мой вариант
KolZak = int(input("Введите количество заказов: "))
BaseZak = {}
print("В ведите данные через пробел в формате: Покупатель _ название пиццы _ количество заказанных пицц")
for i in range(KolZak):
  pokupat, namePiza, kolPizz = input(f'{i+1}-й Заказ: ').split()
  kolPizz=int(kolPizz)
  if pokupat not in BaseZak:
    BaseZak[pokupat]={namePiza:kolPizz}
  elif namePiza in BaseZak[pokupat]:
    BaseZak[pokupat][namePiza]+=kolPizz
  else:
    BaseZak[pokupat][namePiza]=kolPizz
for pokupat in sorted(BaseZak.keys()):
  print(f"Покупатель: {pokupat} ")
  for namePiza in sorted(BaseZak[pokupat].keys()):
    print(f"Пица: {namePiza}, количество: {BaseZak[pokupat][namePiza]} ") 
    
   
  # # Эталонное решение:
# # Ввод количества заказов
# orders_count = int(input('Введите количество заказов: '))
# # Создаем пустой словарь для хранения данных о заказах
# database = dict()
# # Обрабатываем каждый заказ
# for i_order in range(orders_count):
# # Вводим заказ и разбиваем его на части
#   customer, pizza_name, count = input('{} заказ: '.format(i_order + 1)).split()
# # Преобразуем количество в целое число
#   count = int(count)
# # Если покупатель еще не добавлен в словарь
#   if customer not in database:
# # Добавляем покупателя и начальную запись о пицце
#     database[customer] = {pizza_name: count}
#   else:   
# # Если покупатель уже есть
#     if pizza_name in database[customer]:
# # Если пицца уже была заказана ранее, увеличиваем количество
#       database[customer][pizza_name] += count
#     else:
# # Если пицца новая для этого покупателя, добавляемзапись
#       database[customer][pizza_name] = count
# # Сортируем список покупателей в алфавитном порядке и выводиминформацию
# for customer in sorted(database.keys()):
#   print('{}:'.format(customer))
# # Сортируем пиццы по алфавиту и выводим информацию
#   for pizza_name in sorted(database[customer].keys()):
#     print(' {}: {}'.format(pizza_name,database[customer][pizza_name]))