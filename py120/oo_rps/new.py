class Person:
    TITLES = ['Mr', 'Mrs', 'Ms', 'Dr']
    _total_people = 0

    def __init__(self, name, age=63):
        self._name = name
        self._age = age

    def age(self):
        return self._age

mark = Person('Mark')
