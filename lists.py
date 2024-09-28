# import copy


#Списки(List)

# Список в Python — это упорядоченная изменяемая коллекция объектов любого типа. Списки аналогичны массивам в других языках программирования,
# но они могут содержать объекты различных типов (числа, строки, другие списки и т.д.).
#
# Списки создаются с помощью квадратных скобок:
# my_list = []

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
                        #МЕТОДЫ СПИСКОВ(Самые популярные)

                    # 1 -  .append() Добавляет элемент в конец списка.

# my_list = [1, 2, 3]
# my_list.append(4)  # my_list -> [1, 2, 3, 4]

                #2 - .extend() Расширяет список, добавляя все элементы переданного итерируемого объекта
                                            # (например, другого списка).

# my_list = [23, 54, 23, 53, 99]
# other_list = [1, 24, 99]
# my_list.extend(other_list)
# print(my_list)   #[23, 54, 23, 53, 99, 1, 24, 99]

            # 3 - .insert() # Вставляет элемент на заданную позицию в списке. Позиция указывается первым аргументом.

# my_list = [23, 54, 23, 53, 99]
# my_list.insert(3,  62)
# print(my_list)

            #4 - .remove() Удаляет первое вхождение элемента в списке. Если элемент не найден, вызывает ошибку.

# my_list = [23, 54, 23, 53, 99]
# my_list.remove(23)  # [54, 23, 53, 99]
# my_list.remove(23)  # [54, 53, 99]
# print(my_list)

        # 5 - .pop() Удаляет элемент по указанному индексу и возвращает его.
                    # Если индекс не указан, удаляет и возвращает последний элемент.

# my_list = [23, 54, 23, 53, 99]
# my_list.pop() #[23, 54, 23, 53]
# my_list.pop(2) # [23, 54, 53]
# print(my_list)

                    # 6 - .clear() Очищает список, удаляя все элементы.

# my_list = [23, 54, 23, 53, 99]
# my_list.clear() # []
# print(my_list)

                    # 7 - .index() Возвращает индекс первого вхождения указанного элемента.
                                 # Если элемент не найден, вызывает ошибку.

# my_list = [23, 54, 23, 53, 99]
# print(my_list.index(53)) # 3

                    # 8 - .count() Возвращает количество вхождений элемента в списке.

# my_list = [23, 54, 23, 53, 99]
# print(my_list.count(23)) # 2

                    # 9 - .sort() Сортирует элементы списка на месте. По умолчанию сортирует по возрастанию.
                                # Можно передать параметр reverse=True для сортировки по убыванию.

# my_list = [23, 54, 23, 53, 99]
# my_list.sort() # [23, 23, 53, 54, 99]
# my_list.sort(reverse=True) # [99, 54, 53, 23, 23]
# print(my_list)

                    # 10 - .reverse() Разворачивает список в обратном порядке.

# my_list = [23, 54, 23, 53, 99]
# my_list.reverse() # [99, 53, 23, 54, 23]
# print(my_list)

                #11 - .copy() Возвращает поверхностную копию списка.
                      #.copy.deepcopy() Возвращает глубокую копию объекта

# my_list = [23, 54, 23, 53, 99]
# copied_list = my_list.copy()
# deep_copy = copy.deepcopy(my_list)
# my_list.append(11)
# print(my_list)   # [23, 54, 23, 53, 99, 11]
# print(copied_list) # [23, 54, 23, 53, 99]
# print(deep_copy) # [23, 54, 23, 53, 99]
