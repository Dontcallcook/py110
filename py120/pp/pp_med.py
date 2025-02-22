# Question 2

# class InvoiceEntry:
#     def __init__(self, product_name, number_purchased):
#         self._product_name = product_name
#         self._quantity = number_purchased

#     @property
#     def quantity(self):
#         return self._quantity

#     @quantity.setter
#     def quantity(self, new_quantity):
#         self._quantity = new_quantity

# entry = InvoiceEntry('Marbles', 5000)
# print(entry.quantity)         # 5000

# entry.quantity = 10_000
# print(entry.quantity)         # 10_000


# Quantity 3

# class Animal:
#     def speak(self, sound):
#         print(sound)

# class Cat(Animal):
#     def meow(self):
#         self.speak('Meow!')

# class Dog(Animal):
#     def bark(self):
#         self.speak('Woof! Woof! Woof!')

# cat1 = Cat()
# dog1 = Dog()

# cat1.meow()
# dog1.bark()


# Question 4

# class KrispyKreme:
#     def __init__(self, filling, glazing):
#         self.filling = filling
#         self.glazing = glazing

#     def __str__(self):
#         if not self.filling and not self.glazing:
#             return f'Plain'
#         if not self.filling:
#             return f'Plain with {self.glazing}'
#         if not self.glazing:
#             return self.filling

#         return f'{self.filling} with {self.glazing}'


# donut1 = KrispyKreme(None, None)
# donut2 = KrispyKreme('Vanilla', None)
# donut3 = KrispyKreme(None, 'sugar')
# donut4 = KrispyKreme(None, 'chocolate sprinkles')
# donut5 = KrispyKreme('Custard', 'icing')

# print(donut1)       # Plain
# print(donut2)       # Vanilla
# print(donut3)       # Plain with sugar
# print(donut4)       # Plain with chocolate sprinkles
# print(donut5)       # Custard with icing


# Question 5

# class Light:
#     def __init__(self, brightness, color):
#         self.brightness = brightness
#         self.color = color

#     def status(self):
#         return (f'I have a brightness level of {self.brightness} '
#                 f'and a color of {self.color}')

# my_light = Light(50, 'Red')
# print(my_light.status())