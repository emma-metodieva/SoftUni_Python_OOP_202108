# from animal import Animal
# from bear import Bear
# from gorilla import Gorilla
# from lizard import Lizard
# from mammal import Mammal
# from reptile import Reptile
# from snake import Snake
from project.lizard import Lizard
from project.mammal import Mammal

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
