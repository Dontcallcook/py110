# class Student:

#     def __init__(self, first_name, last_name, grade):
#         self._first_name = first_name
#         self._last_name = last_name
#         self._grade = self.grade_validation(grade)

#     @property
#     def full_name(self):
#         return f'{self._first_name.title()} {self._last_name.title()}'

#     @full_name.setter
#     def full_name(self, names):
#         if not isinstance(names, tuple) or len(names) < 2:
#             raise ValueError('Student\'s name must include two names')
#         self._first_name, self._last_name = names

#     @property
#     def grade(self):
#         return f'{self.full_name}\'s grade is {self._grade}'

#     @grade.setter
#     def grade(self, grade):
#         self._grade = self.grade_validation(grade)

#     @staticmethod
#     def grade_validation(grade):
#         if not isinstance(grade, (int, float)) or grade < 0 or grade > 100:
#             raise ValueError('Grade needs to be an integer between 0-100')

#         return grade

# student = Student("john", "doe", 85)
# print(student.full_name)  # "John Doe"
# student.full_name = ("jane", "smith")
# print(student.full_name)  # "Jane Smith"
# student.grade = 105  # Should raise a ValueError

# class Car:

#     def __init__(self, speed, color, fuel):
#         self._speed = speed
#         self._color = color
#         self._fuel = fuel

#     @property
#     def speed(self):
#         return self._speed
    
#     @speed.setter
#     def speed(self, new_speed):
#         if not isinstance(new_speed, (int)) or new_speed < 0: 
#             raise ValueError('Speed must be an integer above 0!')
#         self._speed = new_speed
    
#     @property
#     def fuel(self):
#         return self._fuel
    
#     @fuel.setter
#     def fuel(self, new_fuel):
#         if not isinstance(new_fuel, (int)) or new_fuel < 0:
#             raise ValueError('Fuel must be an integer above 0!')
#         self._fuel = new_fuel

#     def accelerate(self):
#         if self._fuel < 1:
#             print(f'Can\'t accelerate: You\'re out of fuel!')
#             return 
#         self._fuel -= 1
#         self._speed += 10

#     def brake(self):
#         if self._speed == 0:
#             print(f'Can\'t brake: You\'re speed is already 0!')
#             return 
#         elif self._speed < 10:
#             self._speed = 0
#         else:
#             self._speed -= 10

# my_car = Car(200, 'red', 0)
# my_car.accelerate()
# print(my_car.speed)
# my_car.brake()
# print(my_car.speed)

class Person:

    def __init__(self, first_name, last_name):
        self.name = (first_name, last_name)
    
    @property
    def name(self):
        return f'{self._first_name.title()} {self._last_name.title()}'
    
    @name.setter
    def name(self, names):
        self._first_name = self.validate_name(names[0])
        self._last_name = self.validate_name(names[1])
    
    @staticmethod
    def validate_name(name):
        if not isinstance(name, str) or not name.isalpha():
            raise ValueError('Name must be alphabetic.')
        return name

character = Person('annIE', 'HAll')
print(character.name)          # Annie Hall
character = Person('David', 'Meier')
# ValueError: Name must be alphabetic.
