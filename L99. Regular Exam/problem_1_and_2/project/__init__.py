from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.bakery import Bakery
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable

if __name__ == "__main__":
    bakery = Bakery("My Bakery")

    bakery.add_table("InsideTable", 1, 4)
    bakery.add_table("OutsideTable", 51, 6)
    bakery.add_food("Bread", "Eliaz", 1.50)
    bakery.add_food("Cake", "Nedelya", 5.50)
    bakery.add_drink("Water", "Spring", 500, "Bankya")
    bakery.add_drink("Tea", "Peppermint", 250, "Pickwick")

    print(bakery.order_food(1, "Eliaz", "Nedelya", "Something"))
