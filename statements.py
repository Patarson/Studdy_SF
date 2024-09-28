                        #Условные инструкции(Statement) if\elif\else
#
# if Условие:
#     #Блок кода,выполняемый
#     #однократно,если Условие правдиво.
#
# my_num = 22
#
# if my_num > 0:
#     print('Число больше нуля')
#
# person_info = {
#     'age': 20,
# }
#
# if not person_info.get('name'): #Пытаемся получить ключ 'name' из словаря person_info
#     print('Имя отсутствует') # Если его нету выводим сообщение в терминал
#     # 1 Ключа 'name' у объекта нету
#     # 2 Ключ 'name' есть,но его значение ложно
#
#
# num_one = 10
# num_two = 5
#
# if (num_one > 0 and
#     num_two > 0 and
#     isinstance(num_one, int) and
#     isinstance(num_two, int)):
#     print('Both numbers are ints and positive')
#
                             #Задача
#
# my_dict = {
#     'distance': 2300
# }
#
# my_s_dict = {
#     'speed': 20,
#     'time' : 6,
# }
#
# my_third_dict = {
#
# }
#
# def route_info(**route):
#     if ('distance' in route) and (type(route['distance']) == int): #Синтаксис для работы с ключами словарей
#         return f"Distance to your destination is {route['distance']}"
#         #Distance to your destination is 2300
#     if ((('speed' in route) and
#          ('time' in route) and
#          (type(route['speed']) == int)) and
#             (type(route['time']) == int)):
#         return f"Distance to your destination is {route['speed'] * route['time']} "
#         #Distance to your destination is 120
#     return 'No distance info is available'
#     #No distance info is available
#
# print(route_info(**my_dict))
# print(route_info(**my_s_dict))
# print(route_info(**my_third_dict))

                                            #Тернарные операторы

# my_img = ('1920', '1080')
# if len(my_img) == 2:
#     print(f"{my_img[0]}x{my_img[1]}")
# else:
#     print('Incorrect img format')
# print('String is long' if len(str(my_img)) > 79 else 'Sting is short')
# # info = f"{my_img[0]}x{my_img[1]}" if len(my_img) == 2 else 'Incorrect img format'
# # print(info)
#
