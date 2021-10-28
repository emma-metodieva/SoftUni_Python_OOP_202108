class Room:
    def __init__(self, name, budget, members_count):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self._expenses = 0

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self._expenses = value

    def calculate_expenses(self, *args):
        total_expenses = 0
        for arg in args:
            for element in arg:
                total_expenses += element.cost * 30
        self.expenses = total_expenses

class Child:
    def __init__(self, food_cost, *toy_costs):
        self.cost = food_cost + sum(toy_costs)

class Fridge:
    pass

# from project.people.child import Child
# from project.rooms.room import Room
# from project.appliances.fridge import Fridge
# class Imports:
#     pass
