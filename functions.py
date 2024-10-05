                            #ФУНКИЦЯ ZIP

# fruits = ['apple', 'banana', 'lime']
#
# qty = [100, 70, 50]
#
# fruits_qtys_zip = zip(fruits, qty) # Обьеденяет обьекты в 1,может быть любого типа
#
# print(fruits_qtys_zip)
#
# print(type(fruits_qtys_zip))
#
# fruit_qtys_dict = dict(fruits_qtys_zip)
#
# print(fruit_qtys_dict)

                        # ФУНКЦИИ В PYTHON

# Функция это блок кода,который можно выполнять многократно

# def my_fn(a, b):
#     a = a + 1
#     c = a + b
#     return c
#
#
# res = my_fn(3, 5)
#
# print(res)

#                                           #Задача

# def merge_list_to_dict(list_one, list_two):
#     merge = zip(list_one, list_two)
#     list_to_dict = dict(merge)
#     return list_to_dict
#
#
# res = merge_list_to_dict(['Brand', 'Model', 'Price'], ['Apple', 'IPhone 12', 1200])
# print(res)

                                        #Задача № 1

# def merge_list_to_dict(list_one, list_two):
#     return dict(zip(list_one, list_two))
#
#
# res_one = merge_list_to_dict(list_one=['Brand', 'Model', 'Price'], list_two=['Apple', 'IPhone 12', 1200])
#
# print(res_one)
#
# res_two = merge_list_to_dict(list_two=['Apple', 'IPhone 12', 1200], list_one=['Brand', 'Model', 'Price'])

                # #Если оба аргумента именованные порядок следования не важен.

# print(res_one)
#
# res_three = merge_list_to_dict(['Brand', 'Model', 'Price'], list_two=['Apple', 'IPhone 12', 1200])
#               #Сначала идёт позиционный аргумент,и только потом именованный,иначе ошибка
# print(res_three)
#    #Задача № 2

# def update_car_info(**car): #Создаём функцию которая принимать в себя только аргументы с ключевыми словами.
#     car['is_available'] = True # Добавляем в словать новую пару ключ - значение
#     return car
#
#
# print(update_car_info(brand='BMW', price=10000)) # Вызываем функицию и передаём ей нужные нам аргументы с ключевыми словами.

#                                           Значения функции по умолчанию:
#
# def mult_by_factor(value, multiplier=1):  # multiplier - необязательный аргумент,так как в функции он установлен по умолчанию = 1.
#     return value * multiplier  #Часто значению по умолчанию присваивают None,если хотят сделать его необязательным.
#
#
# print(mult_by_factor(5))
# #Выведет = 5
# print(mult_by_factor(5, 25))
# # Здесь параметр по умолчанию изменяется

# from datetime import date
#
#
# def get_weekday():
#     return date.today().strftime('%A')
#
#
# def create_new_post(post, weekday=get_weekday()):
#     post_copy = post.copy()
#     post_copy['created_on_weekday'] = weekday
#     return post_copy
#
#
# initial_post = {
#     'id': 243,
#     'author': 'Robert'
# }
#
# post_with_weekday = create_new_post(initial_post)
#
# print(post_with_weekday)
                                        #Callback Function
                #Функция,которая передаётся как аргумент в другую функцию,и там вызывается.

# def other_fn():
#     pass
#
#
# def fn_with_callback(callback_fn): #В теле этой функции вызывается другая функция.
#     callback_fn() #Пример.
#
#
# fn_with_callback(other_fn()) # Вызываем функцию с callback и передаём ей другую функцию.
#
# def print_num_info(num):
#     if (num % 2) == 0:
#         print('Entered number is even')
#     else:
#         print('Entered number is odd')
#
#
# def print_square_num(num):
#     print('Square of the num is', num * num)
#
#
# def process_number(num, callback_fn):
#     callback_fn(num)
#
#
# entered_num = int(input('Enter any number: '))
#
# process_number(entered_num, print_num_info)
# process_number(entered_num, print_square_num)


# def send_date(data):
#     pass
#
#
# def process_data(input_data, send_data_fn):
#     update_data = input_data.copy()
#     send_data_fn(update_data)
#
#
# process_data({'Name': 'Robert'}, send_date)

                                # Правила работы с функциями

# 1.Называть функции исходя из выполняемых задач

# 2.Название функции начинать с глагола

# 3.Одна функция должна выполнять одну задачу

# 4.Не рекомендуется изменять внешние относительно функции переменные

                                # Документация функции(Dockstring)

# # Синтаксис
# def mult_by_factor(value, mult=1):
#     """Multiplies number by multiplicator"""   #Коментарий как работает функция
#     return value * mult
#
#
# print(mult_by_factor(5, 25))

                                            #Области видимости
                                          #Глобальные и локальные

# a = 10  # Глобальная переменная и область видимости
#
#
# def my_fn():
#     global a  # Перезаписывает переменную а из глобальной области видимости
#     a = True  # Локальная
#     b = 15  # Область
#     print(a)  # Видимости  #  True
#     print(b)  # Функции  # 15
# #
# #
# my_fn()
#
# print(a)  #True так как в функции мы перезаписали глобальную переменную
# print(b) # NameError: name 'b' is not defined переменная b объявлена в области видимости функции

# c = 5
# #
# #
# # def my_fn(a, b):
# #     d = 10
# #     print(c)
# #     print(a, b, d)
# #     print(dir())  # Показывает какие переменные доступны в текущей области видимости
# #
# #
# # print(dir())
# #
# #
# # my_fn('abc', 'xyz')
# #
# # # print(a)  # NameError: name 'a' is not defined

                                    #Lambda function

# def mult(a, b):
#     return a * b
#
#
# multi = lambda a, b: a * b  #Не рекомендруется лямбда функции присваивать именам переменных
#
# print(multi)
#

# def greeting(greet):
#     return lambda name: f'{greet}, {name}!' #Пример применения лямбда функции
#
#
# morning_greeting = greeting('Good Morning')
#
# print(morning_greeting('Robert'))
#
# evening_greeting = greeting('Good Evening')
#
# print(evening_greeting('Denys'))

                                    # Оператор yield
# Оператор yield в Python используется в генераторах — это специальные функции, которые позволяют поэтапно возвращать значения без полного завершения выполнения функции.
            #В отличие от обычной функции с оператором return, генератор сохраняет своё текущее состояние между вызовами, что позволяет возобновлять его работу с места остановки.
            #Это особенно полезно при работе с большими объемами данных, где не нужно сразу загружать всё в память.

                                    #  Как работает yield
        # Когда функция содержит оператор yield, она становится генератором.
        # Вызов такой функции не выполняет её сразу, а возвращает объект-генератор.
        # Значения из этого генератора можно получать по одному с помощью методов вроде next() или в цикле for.

# def fib():
#     a, b = 0, 1
#     yield a # 0
#     yield b # 1
#
#     while True:
#         a, b = b, a + b
#         yield b
#
#
# for num in fib():   # бесконечный цикл который будет возвращать новое число Фибоначчи из фукнкции fib()
#     print(num)
