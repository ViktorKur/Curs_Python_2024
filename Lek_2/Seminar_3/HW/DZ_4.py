# Задача 4. Товары В базе данных магазина вся необходимая информация по товарам делится на два словаря: 
# первый отвечает за коды товаров, второй — за списки количества разнообразных товаров на складе:
#   goods = { 'Лампа': '12345', 'Стол': '23456', 'Диван': '34567', 'Стул': '45678', } 
#   store = { '12345': [ {'quantity': 27, 'price': 42}, ], '23456': [ {'quantity': 22, 'price': 510},
#   {'quantity': 32, 'price': 520}, ], '34567': [ {'quantity': 2, 'price': 1200}, {'quantity': 1, 'price': 1150}, ],
#   '45678': [ {'quantity': 50, 'price': 100},{'quantity': 12, 'price': 95}, {'quantity': 43, 'price': 97}, ], } 
#   Каждая запись второго словаря отображает, сколько и по какой цене закупалось товаров. Цена указана за одну штуку.
#   Напишите программу, которая рассчитывает общую стоимость позиций для каждого товара на складе и выводит эту информацию на экран. 
#   Результат работы программы: Лампа —27штук, стоимость 1134 рубля. Стол —54штуки, стоимость 27 860 рублей. Диван — 3штуки, стоимость 3550 рублей. 
#   Стул —105 штук, стоимость 10 311 рублей.
goods = { 'Лампа': '12345', 'Стол': '23456', 'Диван': '34567', 'Стул': '45678', } 
store = { '12345': [ {'quantity': 27, 'price': 42}, ], '23456': [ {'quantity': 22, 'price': 510},
{'quantity': 32, 'price': 520}, ], '34567': [ {'quantity': 2, 'price': 1200}, {'quantity': 1, 'price': 1150}, ],
'45678': [ {'quantity': 50, 'price': 100},{'quantity': 12, 'price': 95}, {'quantity': 43, 'price': 97}, ], } 
for Tov, art in goods.items():
  # print (Tov,art)
  SumKol=SumCena=0
  for param_art in store[art]:
    # print(param_art)
    SumCena=SumCena+param_art['quantity']*param_art['price']
    SumKol=SumKol+param_art['quantity']
  print(f"{Tov} - {SumKol} штук, суммарная стоимость: {SumCena} руб.")
    
#  # ЭТАЛОННОЕ РЕШЕНИЕ  
# goods = { 'Лампа': '12345', 'Стол': '23456', 'Диван': '34567', 'Стул': '45678', } 
# store = { '12345': [ {'quantity': 27, 'price': 42}, ], '23456': [ {'quantity': 22, 'price': 510},
# {'quantity': 32, 'price': 520}, ], '34567': [ {'quantity': 2, 'price': 1200}, {'quantity': 1, 'price': 1150}, ],
# '45678': [ {'quantity': 50, 'price': 100},{'quantity': 12, 'price': 95}, {'quantity': 43, 'price': 97}, ], }     
# # Проходим по всем товарам в словаре goods
# for item_name in goods.keys():
#   print(item_name)
# # Получаем код товара из словаря goods
#   item_code = goods[item_name]
# # Инициализируем переменные для подсчета общего количества и стоимости
#   total_quantity = 0
#   total_cost = 0
# # Проходим по всем записям для данного товара в словаре store
#   for entry in store[item_code]:
#     print (entry)
# # Увеличиваем общее количество товара
#     total_quantity += entry['quantity']
# # Увеличиваем общую стоимость товара
#     total_cost += entry['price'] * entry['quantity']
# # Выводим информацию о товаре
#   print('{} — {} штук, стоимость {} рубля(ей).'.format(item_name,total_quantity, total_cost))

