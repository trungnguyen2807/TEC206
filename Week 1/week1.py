# age = 25
# print(type(age)) # Output: <class 'int'>
# name = "John"
# print(type(name)) # Output: <class 'str'>
# price = 9.99
# print(type(price)) # Output: <class 'float'>
# is_student = True
# print(type(is_student)) # Output: <class 'bool'>


class Car:
  def __init__(self, brand, color):
    self.brand = brand 
    self.color = color

  def printDetails(self):
    return str(self.brand) + ' ' + str(self.color)
    # print(f'{self.brand} {self.color}')
car1 = Car(1, 1)
car2 = Car(2, 2)

car1.printDetails()
car2.printDetails()





    