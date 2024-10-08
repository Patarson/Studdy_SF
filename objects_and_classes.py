# import datetime


                                # ООП в Python

            # Объектно-ориентированное программирование (ООП) в Python — это парадигма программирования,
            # которая основывается на концепции объектов.
            # Объекты — это экземпляры классов, которые могут содержать данные (атрибуты) и функции (методы),
            # позволяя организовывать код более структурировано и удобно для поддержки.

                        # Конструкция if __name__ == "__main__"

#  Конструкция if __name__ == "__main__": — это стандартный способ проверки в Python,
#  которая определяет, был ли файл запущен напрямую как отдельный скрипт или был импортирован как модуль в другой файл.
#  Эта конструкция используется для того, чтобы выполнять определённый код только в том случае, если файл запускается напрямую.
#  Пример в файлах myclass.py and main.py

# class MyClass:
#    def f(self):
#        return 155
#
#
# mc2 = MyClass()  #Обозначаем обьект класса
# print("It's for test too", mc2.f())  # It's for test too 155
#
#
# if __name__ == "__main__":
#    mc = MyClass()
#    print("It's only for test", mc.f()) # It's only for test 155

                                #Подведем итог:

# код в конструкции if __name__ == "__main__":  будет выполняться только при запуске файла, в котором он находится.
# Это очень удобно, когда вы хотите протестировать классы в отдельных файлах или переиспользовать код одного из файлов,
# не удаляя из него вызовы функций и объявления классов.


                                # Синтаксис:

# class Car:
#     def __init__(self, brand, model): #Иницилизурием класс с 2мя атрибутами
#         self.brand = brand  # Бренд
#         self.model = model  # Модель
#
#     def start_engine(self):  #  Метод класса Car
#         print(f"The car of {self.brand} {self.model} is starting.")
#
#     def display_info(self):  #Ещё 1 метод
#         print(f"Car: {self.brand} {self.model}")
#
#
# my_car = Car('Toyota', 'Camry')
# my_car.start_engine()  # The car of ToyotaCamry is starting.
# my_car.display_info()   # Car: Toyota Camry

# class Event:
#     def __init__(self, timestamp, event_type, session_id): # 1.1 Можно либо установить значение по умолчанию.Пример: timestamp=0
#         self.timestamp = timestamp # Инициируем атрибуты класса
#         self.event_type = event_type
#         self.session_id = session_id
#
#     def init_from_dict(self, event_dict):  #Упростим цикл с помощью метода нашего класса
#         self.timestamp = event_dict.get('timestamp')
#         self.event_type = event_dict.get('type')
#         self.session_id = event_dict.get('session_id')
#
#
# events = [
#     {
#      "timestamp": 1554583508000,
#      "type": "itemViewEvent",
#      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#      "timestamp": 1555296337000,
#      "type": "itemViewEvent",
#      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#      "timestamp": 1549461608000,
#      "type": "itemBuyEvent",
#      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
# ]
#
# # for event in events: # прошлись циклом по списку словарей и получили нужную нам информацию
# #     event_obj = Event(timestamp=event.get('timestamp'), #
# #                       event_type=event.get('type'),
# #                       session_id=event.get('session_id'))
# #     print(event_obj.timestamp)
#
# for event in events:
#     event_obj = Event(*events)  # 1.2  Либо в цикле передать в класс наш словать с оператором распаковки *
#     event_obj.init_from_dict(event)
#     print(event_obj.timestamp)  # 1554583508000  # 1555296337000  # 1549461608000
#
#     print(event_obj.event_type)  # itemViewEvent # itemViewEvent  # itemBuyEvent
#
#     print(event_obj.session_id)   # 0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct
#                                   # 0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct
#                                   # 0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct

                                    # 1.ИНКАПСУЛЯЦИЯ

#Инкапусляция — это один из принципов ООП, который говорит нам о том, что поля и методы должны быть одной целой системой.
                            # Иначе говоря, работаем с полями класса только через методы.

# class Human:
#     age = None
#
#     def __init__(self, age=4):
#         self.age = age
#
#     def get_age(self):   #Добавляем геттер - специальный метод для получения поля
#         return self.age
#
#     def set_age(self, age):  # добавляем сеттер - специальный метод для установки нового значения
#         try:  # Добавим отлов ошибки
#             if age > 0 and isinstance(age, int):  # проверяем условия, что человеку должно быть больше 0 лет и его возраст - целое число
#                 self.age = age
#         except TypeError:   #Если число отрицательно - используется значение по умолчани,если же там строка- отлавливаем ошибку TypeError
#             print('Должно быть число')
#
#
# h = Human()
# h.set_age(-2)
# print(h.get_age())

                                    # 2.НАСЛЕДОВАНИЕ

        #Наследование позволяет одному классу (наследнику) унаследовать свойства и методы другого класса (родителя).
                            # Это способствует повторному использованию кода.


# class Product:   #Создаём класс Продукт.
#     max_qty = 10000   # Устанавливаем максимальное количество.
#
#     def __init__(self, name, category, qny_in_stock):  #инициируем имя,категорию и количество в магазине.
#         self.name = name
#         self.category = category
#         self.qty_in_stock = qny_in_stock
#
#     def is_available(self):   #Создаём метод который проверяет доступен ли продукт.
#         return True if self.qty_in_stock > 0 else False # Вернуть True если количство больше 0,иначе False
#
#
# class Food(Product):   #Создаём класс Food который является наследником класса Product
#     is_critical = True  # Указываем что продукт важен
#     need_to_refresh = True  # Указываем что продукт нужно обновлять
#     refresh_frequency = datetime.timedelta(days=1)  # С переодичностью 1 день
#
#
# eggs = Food('eggs', "food", 5) #Создаём объект eggs как экземпляр класса Food
# print(eggs.is_available())  # True
# print(eggs.name)  # eggs
# print(eggs.category)   # food
# print(eggs.max_qty)  # 10000

                            # 3.ПОЛИМОРФИЗ

# Полиморфизм — это способность объектов разных классов использовать один и тот же интерфейс (методы).
# Разные классы могут реализовывать один и тот же метод по-разному.

# class Animal:
#
#     def speak(self):
#         print('Some sound')
#
#
# class Dog(Animal):
#     def speak(self):
#         print('Bark')
#
#
# class Cat(Animal):
#     def speak(self):
#         print('Meow')
#
#
# animals = [Dog(), Cat()]
# for animal in animals:
#     animal.speak()  # Bark  # Meow


            # Еще немного о полиморфизме и магических методах на примере __eq__ и __str__

#   __eq__ — определяет поведение оператора равенства ==;
#   __str__ — определяет поведение функции str() или вызов внутри функции print().

# class Dot:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):  # Проверяем равенство между параметрами
#         return self.x == other.y and self.y == other.y
#
#     def __str__(self):  #Конвертируем результат в строку
#         return f"Dot: {self.x, self.y}"
#
#
# p1 = Dot(1, 2)  # Присваиваем обьекты класса
# p2 = Dot(1, 2)  # Присваиваем обьекты класса
#
# print(p1 == p2)    # Проверяем равенство == False
# print(str(p1))   # Dot: (1, 2)
# print(p2)    # Dot: (1, 2)

                        # Задание 1.10.

# Создайте класс одной из геометрических фигур (например, прямоугольника), где в конструкторе задаются атрибуты:
# начальные координаты x, y, width и height (или другие в зависимости от выбранной фигуры).
# Создайте метод, который возвращает атрибуты прямоугольника как строку ( постарайтесь применить магический метод __str__).
# Для объекта прямоугольника со значениями атрибута x = 5, y = 10, width = 50, height = 100 метод должен вернуть строку Rectangle : 5, 10, 50, 100.

# class Rectangle:
#     def __init__(self, x, y, width, height): #Инициируем параметры
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#     def __str__(self):  # Возвращаем полученные параметры в виде строки
#         return f"Rectangle: {self.x}, {self.y}, {self.width}, {self.height}"  #
#
#
# react_1 = Rectangle(5, 10, 50, 100)
# print(react_1)

                        # Задание 1.10.2

# В классе, написанном в предыдущем задании, создайте метод, который будет рассчитывать площадь фигуры. Выведите значение площади на экран.

# class Rectangle:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#     def __str__(self):
#         return f"Rectangle: {self.x}, {self.y}, {self.width}, {self.height}"
#
#     def get_area(self):  #Рассчитываем площадь фигуры по формуре  S = a × h, где a — сторона, h — высота
#         return self.width * self.height
#
#
# react_1 = Rectangle(5, 10, 50, 100)
# print(react_1)
# print(react_1.get_area())


                            # Задание 1.10.3
#В проекте «Дом питомца» добавим новую услугу — электронный кошелек. Необходимо создать класс «Клиент», который будет содержать данные о клиентах и их финансовых операциях.
# О клиенте известна следующая информация: имя, фамилия, город, баланс.
#Далее сделайте вывод о клиентах в консоль в формате:

# «Иван Петров. Москва. Баланс: 50 руб.»


# class Client:
#     def __init__(self, name, surname, city, balance):  #Инициируем параметры
#         self.name = name  # Имя
#         self.surname = surname # Фамилия
#         self.city = city # Город
#         self.balance = balance # Баланс
#
#     def __str__(self):   #Возвращаем результат в виде строки с данными
#         return f'{self.name} {self.surname}.\nCity: {self.city}.\nBalance: {self.balance} RUB'
#
#
# person = Client('Ivan', 'Petrov', 'Moscow', 50)
# print(person)


                            # Задание 1.10.4


# Команда проекта «Дом питомца» планирует большой корпоратив для своих клиентов.
# Вам необходимо написать программу, которая позволит составить список гостей.
# В класс «Клиент» добавьте метод, который будет возвращать информацию только об имени, фамилии и городе клиента.

# Затем создайте список, в который будут добавлены все клиенты, и выведете его в консоль.

# class Client:
#     def __init__(self, name, surname, city, balance):
#         self.name = name
#         self.surname = surname
#         self.city = city
#         self.balance = balance
#
#     def __str__(self):
#         return f'{self.name} {self.surname}.City: {self.city}.Balance: {self.balance} RUB'
#
#     def get_quest(self):   # Добавляем метод который возвращает только имя,фамилию и город
#         return f'{self.name} {self.surname}. City: {self.city}.'


# customer_1 = Client('Denys', 'Patarson', 'Kanada', 1200)
# customer_2 = Client('Ivan', 'Petrov', 'Moscow', 100)
# customer_3 = Client('Katrin', 'Ashanina', 'Moscow', 1200)
#
# customer_lists = [customer_3, customer_2, customer_1] # Добавляем всех гостей в список
# for quest in customer_lists:    #Проходим циклом по гостям из нашего списка
#     print(quest.get_quest())   # И выводим нужную информацию из метода get_quest()
