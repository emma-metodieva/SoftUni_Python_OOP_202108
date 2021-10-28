from project.appliances.appliance import Appliance
from project.people.child import Child


class Room:
    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.room_cost = 0
        self.expenses = 0

    @property
    def monthly_consumption(self):
        return self.room_cost + self.expenses

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    @staticmethod
    def calculate_expenses(*args):
        expenses = 0
        for list_of_objects in args:
            for instance in list_of_objects:
                if isinstance(instance, Appliance):
                    expenses += instance.get_monthly_expense()
                else:
                    expenses += instance.cost * 30
        return expenses
