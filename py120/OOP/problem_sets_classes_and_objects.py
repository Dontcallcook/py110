class Person:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'
    
    @name.setter
    def name(self, new_name):
        parts = new_name.split()
        self.first_name = parts[0]
        self.last_name = parts[1] if len(parts) > 1 else ''

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, name):
        self._first_name = name
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, name):
        self._last_name = name

    def __eq__(self, other):
        return self.name == other.name

bob = Person('Robert Smith')
rob = Person('Robert Smith')

print(bob == rob)