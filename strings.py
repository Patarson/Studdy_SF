                                    # Строки в Python
# В Python строки (тип str) — это упорядоченные последовательности символов, заключенные в одинарные ('...') или двойные кавычки ("...").
# Строки неизменяемы (immutable), что означает, что после создания строку нельзя изменить.



                                    #Методы строк в Python:

            # 1 - len() — Возвращает длину строки (количество символов).

# s = "Python"
# print(len(s))  # 6

            # 2 - lower() — Преобразует строку в нижний регистр.

# s = "PYTHON"
# print(s.lower())  # python

#             3 - upper() — Преобразует строку в верхний регистр.

# s = "python"
# print(s.upper())  # PYTHON

             # 4 - capitalize() — Преобразует первый символ строки в верхний регистр.

# s = "python"
# print(s.capitalize())  # Python

            #5 - title() — Преобразует первые буквы всех слов в строке в верхний регистр.
#
# s = "привет мир"
# print(s.title())  # Привет Мир

            # 6 - strip() — Убирает пробелы или символы по краям строки.

# s = "   Python   "
# print(s.strip())  # 'Python'

            # 7 - replace(old, new) — Заменяет все вхождения подстроки old на new.

# s = "Hello, World!"
# print(s.replace("World", "Python"))  # Hello, Python!

            # 8 - split(separator) — Разбивает строку на список подстрок по указанному разделителю.

# s = "apple,banana,orange"
# print(s.split(","))  # ['apple', 'banana', 'orange']

            # 9 - join(iterable) — Объединяет элементы из итерируемого объекта в строку, используя строку-разделитель.

# fruits = ['apple', 'banana', 'orange']
# print(", ".join(fruits))  # apple, banana, orange

            # 10 - find(substring) — Возвращает индекс первого вхождения подстроки или -1, если подстрока не найдена.

# s = "Hello, World!"
# print(s.find("World"))  # 7

            # 11 - startswith(prefix) и endswith(suffix) — Проверяют, начинается или заканчивается строка указанной подстрокой.

# s = "Hello, World!"
# print(s.startswith("Hello"))  # True
# print(s.endswith("World!"))   # True

            # 12 - isdigit() — Проверяет, состоит ли строка только из цифр

# s = "12345"
# print(s.isdigit())  # True

            # 13 - isalpha() — Проверяет, состоит ли строка только из букв.

# s = "Python"
# print(s.isalpha())  # True

                                #Срезы

# Срез — это подмножество элементов итерируемого объекта, которое задаётся следующим образом:
#
# mystr[START:STOP:STEP] — берёт срез от номера START до STOP, не включая его, с шагом STEP. По умолчанию START=0, STOP=длина объекта, STEP= 1

s = 'Hello,my studdy page!'
print(s[::])
                                    #Соединение строк

# # Самый простой вариант - конкантинация строк = 'Hello ' + 'Python'
# # # f-stings # так же можно обьединять переменные в 1 выводе
# name = 'Robert'
# say = 'Hello'
# print(f'{name} says:{say}')