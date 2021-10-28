# from animal import Animal
from project.animal import Animal


class Cat(Animal):
    @staticmethod
    def meow():
        return "meowing..."
