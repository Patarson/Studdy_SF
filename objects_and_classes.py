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

                            # 4.ПОЛИМОРФИЗ

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

