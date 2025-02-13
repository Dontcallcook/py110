class Pet:
    def __init__(self, name, age, color):
        self._name = name
        self._age = age
        self._color = color

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age
    
    @property
    def color(self):
        return self._color

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)
    
    @property
    def info(self):
        return f'My cat {self._name} is {self._age} years old and has {self._color} fur.'

cocoa = Cat('Cocoa', 3, 'black')
cheddar = Cat('Cheddar', 4, 'yellow and white')

print(cocoa.info)
print(cheddar.info)

# My cat Cocoa is 3 years old and has black fur.
# My cat Cheddar is 4 years old and has yellow and white fur.