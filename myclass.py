class MyClass:
   def f(self):
       return 155


mc2 = MyClass()  #Обозначаем обьект класса
print("It's for test too", mc2.f())  # It's for test too 155


if __name__ == "__main__":
   mc = MyClass()
   print("It's only for test", mc.f()) # It's only for test 155

