                                #Словари(Dict)

                #  Cловари (dict) — упорядоченные наборы объектов, доступных по ключу.
                 #  Иными словами, словарь — это совокупность пар ключ-объект.

# my_dict = {}
#
# print(id(my_dict))
# print(type(my_dict))
#
# my_dict['brand'] = 'Apple' #Добавляем новый ключ и значение с помощью ['имя ключа'] = 'значение'
# my_dict['price'] = 1299
#
# print(my_dict)
# print(id(my_dict))
#
# # print(my_dict.get('type', 'iPhone'))
#
# new_dict = my_dict.copy()
# print(my_dict)
# print(new_dict)
                                    #Создаем словарь из списка списков.

# my_list = [['first', 0], ['second', True]] # Список в которым несколько списков.
# my_dict = dict(my_list) # Конвертируем список в словарь.
#
# print(my_dict) # {'first': 0, 'second': True}

                            #Присвоение ключа и значения с помощью переменных.

# my_dict = {}    # Создаём пустой словарь.
# key_1 = input('key 1: ')    #Просим пользователя ввести ключ.
# value_1 = input('value_1: ')  #Просим пользователя ввести значение.
#
# my_dict[key_1] = value_1    #Вносим в словарь новую пару на основе данных введённых пользователем.
#
# key_2 = input('key 2: ')
# value_2 = input('value_2: ')
#
# my_dict[key_2] = value_2
#
# key_3 = input('key 3: ')
# value_3 = input('value_3: ')
#
# my_dict[key_3] = value_3
#
# print(my_dict)

                        #Распаковка словаря в аргументы с ключевыми словами
#
# user_profile = {
#     'name': 'Robert',
#     'comments_qty': 23,
# }                              #Словарь с данными о пользователе
#
# def user_info(name, comments_qty=0):
#     if not comments_qty:  #Если нету коментариев то используетс значение по умолчанию
#         return f"{name} has no comments"
#
#     return f"{name} has {comments_qty} comments" # Если комментарии есть - возвращаем количество указаных комментариев у пользователя
#
#
# print(user_info(**user_profile))  #Вызываем функцию и передаём ей распакованный словарь

                            # Основные методы Словарей

                # 1. Получение значения по ключу (dict[key])
        # Если ключ существует, вернётся соответствующее значение. Если нет — произойдёт ошибка KeyError.

# my_dict = {
#     'name' : 'John',
#     'age' : 23,
#     'towm' : 'Moscow'
# }
#
# print(my_dict['name'])  # John
# print(my_dict['surname'])  # KeyError: 'surname'

            # 2. Метод get()
            #Возвращает значение по ключу, если он существует.
            #Если ключ отсутствует, можно указать значение по умолчанию.

# my_dict = {
#     'name' : 'John',
#     'age' : 23,
#     'towm' : 'Moscow'
# }
#
# print(my_dict.get('surname', 'Not definied'))   # Not definied
# print(my_dict.get('name', 'Not definied')) # John. Ключ name в словаре существует,и мы его получили

                # 3. Добавление или изменение значений (dict[key] = value)
                # Если ключ существует, значение будет обновлено.
                # Если ключ отсутствует, пара ключ-значение будет добавлена.

# my_dict = {
#     'name' : 'John',
#     'age' : 23,
#     'towm' : 'Moscow'
# }
#
# my_dict['name'] = 'Robert' # {'name': 'Robert', 'age': 23, 'towm': 'Moscow'}
# print(my_dict)
# my_dict['surname'] = 'Patarson' # {'name': 'Robert', 'age': 23, 'towm': 'Moscow', 'surname': 'Patarson'}
# print(my_dict)

                # 4. Метод update()
                # Обновляет словарь значениями из другого словаря или переданными парами ключ-значение.

# my_dict = {
#     'name' : 'John',
#     'age' : 23,
#     'towm' : 'Moscow'
# }
#
# print(my_dict)   # {'name': 'John', 'age': 23, 'towm': 'Moscow'}
#
# my_dict.update({"age": 27, "city": "Boston"})
#
# print(my_dict)   # {'name': 'John', 'age': 27, 'towm': 'Moscow', 'city': 'Boston'}

                # 5. Удаление элементов:
                #Метод pop(key): Удаляет элемент по ключу и возвращает его значение.
                # Если ключ не найден, можно указать значение по умолчанию.
#
# my_dict = {
#     'name' : 'John',
#     'age' : 23,
#     'towm' : 'Moscow'
# }
# # print(my_dict)   # {'name': 'John', 'age': 23, 'towm': 'Moscow'}
# # my_dict.pop('123')  # KeyError: '123' #Ошибка ключа,сгерерировало ошибку.
# # my_dict.pop('123', None)  # {'name': 'John', 'age': 23, 'towm': 'Moscow'} # Передали None в качестве второго аргумента,ошибки нет.
# # print(my_dict)
# last_item = my_dict.popitem()  #  ('towm', 'Moscow')    #Удаляет и возвращает последнюю пару ключ-значение
# last_item_2 = my_dict.popitem()  #  ('age', 23)
# last_item_3 = my_dict.popitem()  #  ('name', 'John')
# print(last_item)
# print(last_item_2)
# print(last_item_3)
# print(my_dict) # {}

                # Метод clear(): Очищает словарь.
# my_dict.clear() # {}

                            #Оператор распаковки словаря **
#
# button = {
#     'widht': 200,
#     'text': 'Buy'
# }
#
# red_button = {      #В новый словарь распаковываем другой словать button
#     **button,
#     'color': 'red'  #Добавляем новую пару
# }
#
# print(red_button)  #{'widht': 200, 'text': 'Buy', 'color': 'red'}
#
# print(button)  #{'widht': 200, 'text': 'Buy'}
#
# all_b = button | red_button # оператор | так же объединяет 2 словаря в 1,расположение словарей важен,потом что пара может перезаписаться.
# print(all_b)

