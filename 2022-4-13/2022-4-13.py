class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'My name is {self.name} and i am {self.age} years old')


a = Person("HanBit",24)
a.introduce()

