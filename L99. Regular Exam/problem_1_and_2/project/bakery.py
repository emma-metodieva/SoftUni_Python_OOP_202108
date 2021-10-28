from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value == ' ':
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        food_in_menu = [f.name for f in self.food_menu]

        food_to_add = None
        if food_type == "Bread":
            food_to_add = Bread(name, price)
        elif food_type == "Cake":
            food_to_add = Cake(name, price)

        if food_to_add.name in food_in_menu:
            raise Exception(f"{food_type} {name} is already in the menu!")
        self.food_menu.append(food_to_add)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        drinks_in_menu = [d.name for d in self.drinks_menu]

        drink_to_add = None
        if drink_type == "Tea":
            drink_to_add = Tea(name, portion, brand)
        elif drink_type == "Water":
            drink_to_add = Water(name, portion, brand)

        if drink_to_add.name in drinks_in_menu:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        self.drinks_menu.append(drink_to_add)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        tables_in_repository = [t.table_number for t in self.tables_repository]

        table_to_add = None
        if table_type == "InsideTable":
            table_to_add = InsideTable(table_number, capacity)
        elif table_type == "OutsideTable":
            table_to_add = OutsideTable(table_number, capacity)

        if table_to_add.table_number in tables_in_repository:
            raise Exception(f"Table {table_number} is already in the bakery!")
        self.tables_repository.append(table_to_add)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table_available = None
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table_available = table
                break

        if table_available:
            table_available.reserve(number_of_people)
            return f"Table {table_available.table_number} has been reserved for {number_of_people} people"
        else:
            return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names: str):
        table_ordering = [t for t in self.tables_repository if t.table_number == table_number]
        if len(table_ordering) == 0:
            return f"Could not find table {table_number}"
        table_ordering = table_ordering[0]

        food_in_menu = [f.name for f in self.food_menu]
        food_not_in_menu = []
        food_ordered = []
        for name in food_names:
            if name in food_in_menu:
                food_to_order = [f for f in self.food_menu if f.name == name][0]
                table_ordering.order_food(food_to_order)
                food_ordered.append(food_to_order)
            else:
                food_not_in_menu.append(name)

        output = f"Table {table_number} ordered:\n"
        for food in food_ordered:
            output += food.__repr__()
            output += '\n'
        output += f"{self.name} does not have in the menu:\n"
        output += '\n'.join(food_not_in_menu)

        return output

    def order_drink(self, table_number: int, *drinks_names: str):
        table_ordering = [t for t in self.tables_repository if t.table_number == table_number]
        if len(table_ordering) == 0:
            return f"Could not find table {table_number}"
        table_ordering = table_ordering[0]

        drinks_in_menu = [d.name for d in self.drinks_menu]
        drinks_not_in_menu = []
        drinks_ordered = []
        for name in drinks_names:
            if name in drinks_in_menu:
                drink_to_order = [d for d in self.drinks_menu if d.name == name][0]
                table_ordering.order_drink(drink_to_order)
                drinks_ordered.append(drink_to_order)
            else:
                drinks_not_in_menu.append(name)

        output = f"Table {table_number} ordered:\n"
        for drink in drinks_ordered:
            output += drink.__repr__()
            output += '\n'
        output += f"{self.name} does not have in the menu:\n"
        output += '\n'.join(drinks_not_in_menu)

        return output

    def leave_table(self, table_number: int):
        table = [t for t in self.tables_repository if t.table_number == table_number][0]
        bill = table.get_bill()
        table.clear()
        self.total_income += bill

        return f"Table: {table_number}\n" \
               f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        output = ""
        for table in self.tables_repository:
            if not table.is_reserved:
                output += table.free_table_info()
                output += f"\n"
        return output

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
