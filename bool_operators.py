                                    #ОПЕРАТОРЫ

# a = 10  # Оператор присвоения
# Арифметичиские "+", "-", "*", "/"
# Сравнения  "==", "!=", "<, <=", ">, >="
# Логические "not", "and", "or" "is", "is not", "in", "not in"

# a = 10
# b = a
#
# c = a + b
#
# print(a is b)  # True
# print(c is a)  # False

# my_num = 10
#
# print(+my_num) # + Является показателем того,что переменная является целым числом
#
# my_bool = True
#
# print(+my_bool) # Конвертирует логическое значение в число - 1

                                    #Логические операторы

# not - Всегда возвращает значение типа bool.Чаще всего используют в условных инструкиях if
# and , or - Возвращают значение одного из операндов, не конвертируют результат в логическое значение
       # Примеры not
# not 10  #False
# not 0  #True
# not 'abc'  #False
# not ''  #True
# not True  #False
# not False  #True

                        #Операторы and, or являются операторами котороткого замыкания(short-circuit)

# my_list = [1, 5, 2]

# print(not not my_list)

# other_list = []

# my_dict = {'a': 5}
#
# # print(other_list or my_list)
# print(my_list and my_dict)

# my_list and print('List is not empty') #Вместо условной конструкции if можно использовать and


