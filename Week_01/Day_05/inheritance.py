class Animal:

    def speak(self):
        print("Animal is speaking")

class Dog(Animal):

    def bark(self):
        print("Dog is barking")

dog = Dog()

dog.speak()
dog.bark()