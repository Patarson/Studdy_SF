    #Циклы
# my_list = [23, 45, 592, 120, 35, 99, 53, 29 , 30]
# for i in my_list:
#     print(i)
# # Для словарей:
# my_object = {
#     'x' : 10,
#     'y' : True,
#     'z' : 'abc'
# }
#
# for i in my_object:
#     print(i, my_object[i])  # Если вывесли только i то получим только ключ,если нужно и значение - my_object[i]
# # i = 0
# # while i != 120:
# #     i += 1
# #     print(i)
#
# my_dict = {
#     'id' : 234,
#     'title' : 'test'
# }
#
# # for item in my_dict.items():
# #     k, v = item # выполняем распаковку ключей и значений
# #     print(k, v) # Вывовдим значения в терминал
# #     #или
# for k, v in my_dict.items():
#     print(k,v) # Так проще

#Для наборов,наборы не упорядочный набор элементов
#Задача
#
# def dict_to_list(**dict_to_conv):
#     list_for_conv = []
#     for k, v in dict_to_conv.items():
#         if type(v) == int:
#             v *= 2
#         list_for_conv.append((k, v))
#     return list_for_conv
#
#
#
# # print(dict_to_list({'a': 5, 'b' : [], 'c': 100}))
# print(dict_to_list(**my_object))
# my_list = [35, True, 23, 'abc', False]
#
# def filter_list(lst, tpy):
#     new_list = []
#     for i in lst:
#         if type(i) == tpy:
#             new_list.append(i)
#     return new_list
#
#
# print(filter_list(my_list, int))
# print(filter_list(my_list, str))
# print(filter_list(my_list, bool))

# def filter_list(list_to_filter, value_type):
#     def check_element_type(elem):
#         return isinstance(elem, value_type)
#     return list(filter(check_element_type, list_to_filter))
#
# print(filter_list(my_list, int))
#Логический класс является подклассом класса инт

                        # Цикл while выполняется пока условние правдиво,и блок кода внутри соответсвенно.
# i = 10
#
# while i < 50:
#     i += 5   #Изменяем переменную внутри цикла
#     print(i)
#
# print(i)
#
# while True:
#     answer = input('Enter yes or no')
#     if answer == 'no':
#         break     # Останавливает цикл при выполнении инструкции

# import random
# #
# #
# # random_num = random.randint(1, 5) #Генерируем случайное число.\
# #
# # while True: #Запускаем бесконечный цикл и просим угадать число.
# #     num = int(input('Guess the number from 1 to 5: '))
# #     if num != random_num: # Пока число пользователя не совпадёт со сгенерированым - продолжаем выполнение цикла.
# #         print('Try again')
# #         continue
# #     print('Congratulations!', random_num, '!')  # Когда совпало выводим поздравления и прерываем цикл.
# #     break

#     Задача

# while True:
#     try:
#         num_1 = float(input('Enter 1 number: '))
#         num_2 = float(input('Enter 2 number: '))
#     except ValueError:
#         print('You must enter numbers')
#         continue
#     res = num_1 / num_2
#
#     print(f'Result: {res}')
#
#     answer = input('Do you want to continue? Y/N')
#     if answer == 'N':
#         break
#Сокращённый цикл for .. in .. используется для создани новый последовательностей
                    #Пример 1
# all_nums = [-3, 1, 0, 10, 20 , - 20, 5, -2]
#
# absolute_nums = []
#
# for nums in all_nums:
#     absolute_nums.append(abs(nums))
#
# print(absolute_nums)
# print(all_nums)
                # Пример 2 с сокращённым циклом

# all_nums = [-3, 1, 0, 10, 20 , - 20, 5, -2]
#
# absolute_nums = [abs(num) for num in all_nums]
#
# print(absolute_nums)
# print(all_nums)

                #Формирование нового набора в обычном цикле
#                                    1
# my_set = {1, 10, 15}
#
# new_set = set()
#
# for val in my_set:
#     new_set.add(val * val)
#
# print(new_set)
# print(my_set)
#                                    2
# my_set = {1, 10, 15}
#
# new_set = set(val * val for val in my_set)
#
# print(new_set)
# print(my_set)

#
# my_scores = [10, 7, 14]
#
# scores = {index: elem for index, elem in enumerate(my_scores)} # Словарь на основании списка.Функция enumerate()возвращает индекс элемента и можно этот индекс присвоить ключу.
#
# print(scores)

# my_dict = {
#     'first' : 'fir',
#     'second' : 'sec',
#     'third' : 'thi'
# }
# upp_dict = {k: v.upper() for k, v in my_dict.items()}
#
# print(upp_dict)

# my_motorbike = ['BMW', 'Germany', 'Robert']
#
# bike = [el for el in my_motorbike if len(el) > 3]
#
# print(bike)