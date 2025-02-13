class Pet:
    def speak(self):
        pass

    def sleep(self):
        return 'sleeping!'
    
    def run(self):
        return 'running!'
    
    def jump(self):
        return 'jumping!'

class Dog(Pet):
    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching!'

class Cat(Pet):
    def speak(self):
        return 'meow!'
    
didi = Cat()
disco = Dog()

print(didi.speak())
print(didi.sleep())
print(didi.run())
print(didi.jump())

print(disco.speak())
print(disco.sleep())
print(disco.run())
print(disco.jump())
print(disco.fetch())

print([cls.__name__ for cls in Cat.mro()])