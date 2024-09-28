                                #Словари(Dict)
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
#Создаем словарь из списка списков
# my_list = [['first', 0], ['second', True]]
#
# my_dict = dict(my_list)
#
# print(my_dict)

# my_dict = {}
# key_1 = input('key 1: ')
# value_1 = input('value_1: ')
#
# my_dict[key_1] = value_1 #Присвоение ключа и значения с помощью переменных
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
# }
#
# def user_info(name, comments_qty=0):
#     if not comments_qty:  #Если нету коментариев то используетс значение по умолчанию
#         return f"{name} has no comments"
#
#     return f"{name} has {comments_qty} comments" # Если комментарии есть - возвращаем количество указаных комментариев у пользователя
#
#
# print(user_info(**user_profile))  #Вызываем функцию и передаём ей распакованный словарь