
                                    #Обработка ошибок в Питоне
# try:
#     #Выполнения блока кода
#     print(10 / 0) # Проверяем код
# except ZeroDivisionError: # отлавливаем ошибку деления на 0
#     #Этот блок выполняется в случае возникновения ошибок в блоке try
#     print("Error - Division by zero!") #Выводим сообщение об ошибке пользователю
#
# print('Continue...') #Продолжается вополнение кода.Если бы не отловили ошибку,то код - не выполнится.
# #Получение информации об ошибке
#
# try:
#     print('10' / 0) #  Пробуем разделить строку на число
# except ZeroDivisionError as e:
#     print(type(e))
#     print(dir(e))
#     print(e)
# except TypeError as e: #Отлавливаем допонительную ошибку,так как строка не делиться на число
#     print(e)
#
# print('123')

                            #Блоки else и finally в обработке ошибок


# try:
#     print(10 / '0') #  Пробуем разделить строку на число
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e: #Отлавливаем допонительную ошибку,так как строка не делиться на число
#     print(e)
# else:                              #Этот фрагмент выводится только в том случае,если ошибок не возникло
#     print('There was no error')
# finally:                           #Этот фрагмент выводится в любом случае,вне зависимости возникла ошибка или нет.
#     print('Continue...')


                            #Отсутствие типа ошибки и класс Exception
#
# try:
#     print(10 / 0)
# except Exception as e:  #Родительский класс встроенных ошибок в Python/Универсальный способ обрабатывать все ошибки
#     # print(isinstance(e, ZeroDivisionError))  #Проверяет принадлежность объекта e к тому или иному классу True/False
#     print(e)
#
# finally:
#     print('Continue...')

                                            #Создание ошибок

# def divine_nums(a, b):
#     if b or a == 0:
#         raise TypeError("Second argument can't be 0") #Создаёт тип ошибки внутри функции
#     return a / b
#
#
# try:
#     divine_nums(0, 10)
# # except ZeroDivisionError as e:
# #     print(e)
# except TypeError as e:
#     print(e)
#
# print('Continue...')

    #Задача
# def image_info(img):
#     if ('image_id' not in img) or ('image_title' not in img): #Проверяем есть ли нужные нам ключи в словаре
#         raise TypeError("Keys image_id and image_title must be present") #Если нету,генерируем ошибку TypeError
#     return f"Image {img['image_title']} has id {img['image_id']}"
#
#
# print(image_info({'image_title': 'My cat', 'image_id': 431}))
# #Обрабатываем ошибку с помощью отлова исключений.
# try:
#     print(image_info({'image_title': 'My cat'}))
# except TypeError as e:
#     print(e)


