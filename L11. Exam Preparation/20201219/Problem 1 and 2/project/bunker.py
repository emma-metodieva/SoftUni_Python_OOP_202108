from project.medicine.medicine import Medicine
from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.supply.food_supply import FoodSupply
from project.supply.supply import Supply
from project.supply.water_supply import WaterSupply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_list = [s for s in self.supplies if isinstance(s, FoodSupply)]
        if len(food_list) == 0:
            raise IndexError("There are no food supplies left!")
        return food_list

    @property
    def water(self):
        water_list = [w for w in self.supplies if isinstance(w, WaterSupply)]
        if len(water_list) == 0:
            raise IndexError("There are no water supplies left!")
        return water_list

    @property
    def painkillers(self):
        painkiller_list = [p for p in self.medicine if isinstance(p, Painkiller)]
        if len(painkiller_list) == 0:
            raise IndexError("There are no painkillers left!")
        return painkiller_list

    @property
    def salves(self):
        salves_list = [s for s in self.medicine if isinstance(s, Salve)]
        if len(salves_list) == 0:
            raise IndexError("There are no salves left!")
        return salves_list

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            if medicine_type == "Painkiller":
                medicine_to_apply = self.painkillers.pop()
            else:
                medicine_to_apply = self.salves.pop()
            self.medicine.remove(medicine_to_apply)
            medicine_to_apply.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            if sustenance_type == "Food":
                sustain_to_apply = self.food.pop()
            else:
                sustain_to_apply = self.water.pop()
            self.supplies.remove(sustain_to_apply)
            sustain_to_apply.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2

            food_to_apply = self.food.pop()
            self.supplies.remove(food_to_apply)
            food_to_apply.apply(survivor)

            water_to_apply = self.water.pop()
            self.supplies.remove(water_to_apply)
            water_to_apply.apply(survivor)
