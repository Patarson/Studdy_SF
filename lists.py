                                            #Списки(List)
# my_list = [123, '123', True, 24.5, None]
# my_list.pop(2) # Удаляет по индексу
# print(my_list)
# print(len(my_list)) # Длинна переменной
# my_list.reverse() # Меняет расположение данных в списке
# print(my_list)
# other_list = [False, {'a': 8}]
# my_list.extend(other_list)#Добавляет элементы с одного списка в другой
# print(my_list)

# first_list = [10, True, 'abc']
# second_list = [[1, 2 ], {'b': True}]
# merged_list = first_list + second_list
# print(merged_list)
# other_merged_list = first_list.__add__(second_list)
# print(other_merged_list)


#Распаковка = извлечение значений и присвоение их переменным
#Присвоение по индексу - пример:
# my_fruits = ['apple', 'banana', 'lime']
#
# my_apple = my_fruits[0]
# my_banana = my_fruits[1]
# my_lime = my_fruits[2]
#
# print(my_apple)
# print(my_banana)
# print(my_lime)
#Список и кортежи - упорядочные последовательности элементов
#
# my_fruits = ['apple', 'banana', 'lime'] # С кортежами такой же синтаксис
#
# my_apple, my_banana, my_lime = my_fruits # переменные через запятую,которые будут созданны после выполнения кода,по индексу со списка,по порядку.
#
# print(my_apple)
# print(my_banana)
# print(my_lime)
#
# my_fruits = ['apple', 'banana', 'lime']
#
# my_apple, *rem_fru = my_fruits #*rem_fru создаёт новый список на основанни остатка со старого списка
#
# print(my_apple)
# print(rem_fru)
