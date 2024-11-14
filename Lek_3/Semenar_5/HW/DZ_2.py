# Задача2.Глубокое копирование Вы сделали для заказчика структуру сайта попродаже телефонов:
# site={ 'html':{ 'head':{ 'title': 'Куплю/продамтелефоннедорого' }, 'body':{ 'h2': 'УнассамаянизкаяценанаiPhone', 'div': 'Купить', 'p': ‘Продать' } } }
# Заказчик рассказал своим коллегам на рынке, и они захотели такой же сайт для своих товаров. Вы посчитали, что это лёгкая задача, 
# и быстро принялись за работу. Напишите программу, которая запрашивает у клиента количество сайтов, затем названия продуктов, 
# а после каждого запроса выводит на экран активные сайты. Условия: 
# ● учтите, что функция должна уметь работать с разными сайтами (иначе вам придётся переделывать программу под каждого заказчика заново);
# ● выдолжныполучить список, хранящий сайты для разных продуктов (а значит, для каждого продукта нужно будет первым делом выполнить 
# глубокое копирование сайта). 
# Пример вывода Сколько сайтов: 2 
# Введите название продукта для нового сайта: iPhone 
# Сайт для iPhone: site = { 'html': { 'head': { 'title': 'Куплю/продам iPhone недорого' }, 'body': { 'h2': 'У нас самая низкая цена на iPhone','div': 'Купить', 'p': ‘Продать' } }} 
# Введите название продукта для нового сайта: Samsung 
# Сайт для iPhone: site = { 'html': { 'head': { 'title': 'Куплю/продам iPhone недорого' }, 'body': { 'h2': 'У нас самая низкая цена на iPhone', 'div': 'Купить', 'p': ‘Продать' } } } 
# Сайт для Samsung: site = { 'html': { 'head': { 'title': 'Куплю/продам Samsung недорого' }, 'body': { 'h2': 'У нас самая низкая цена на Samsung','div': 'Купить', 'p': ‘Продать' } } } 
# Обратите внимание, что на первой итерации выводится только один сайт (для iPhone), а на второй итерации — оба сайта (и для iPhone и для Samsung).
# Чтобы это реализовать, нужно сохранять сайты в списке и каждый раз печатать все его элементы.

# # # # # Эталонное решение
import copy #Исходнаяструктурасайта 
site={ 'html':{ 'head':{ 'title':'Куплю/продам телефон недорого' }, 'body':{ 'h2':'У нас самая низкая цена на iPhone', 'div':'Купить', 'p':'Продать' } } } 
#Функциядлязаменызначениявструктуресловаря 
def change_value(struct,key,value): 
  if key in struct: 
    struct[key]=value 
  else: 
    for sub_struct in struct.values(): 
      if isinstance(sub_struct,dict): 
        change_value(sub_struct,key,value) 
        return struct 
#Функция для отображения структуры сайта 
def display_struct(struct,spaces=1): 
  for key,value in struct.items():
    if isinstance(value,dict): 
      print(''*spaces,key) 
      display_struct(value,spaces+3) 
    else: print("{}{}:{}".format(''*spaces,key,value))
#Функциядлясозданиясайтаподконкретныйпродукт 
def make_site(name): 
  struct_site=copy.deepcopy(site) 
  #Глубокоекопирование исходногосайта 
  new_title='Куплю/продам {} недорого'.format(name)
  #Изменяем заголовок 
  struct_site=change_value(struct_site,'title',new_title) 
  new_h2='У нас самая низкая ценана{}'.format(name) 
  # Изменяемзаголовоквторогоуровня 
  struct_site=change_value(struct_site,'h2',new_h2)
  return struct_site 
#Основнаячастьпрограммы 
sites=[] 
sites_count=int(input('Сколько сайтов:')) 
for _ in range(sites_count): 
  product_name=input('Введите название продукта для нового сайта:') 
  new_site=make_site(product_name)
  sites.append(new_site) 
  for i_site in sites: 
    display_struct(i_site)
  
