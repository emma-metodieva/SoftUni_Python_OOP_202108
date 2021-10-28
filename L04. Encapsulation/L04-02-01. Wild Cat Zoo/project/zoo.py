class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity > len(self.animals):
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        worker = [worker for worker in self.workers if worker.name == worker_name]
        if worker:
            self.workers.remove(worker[0])
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = 0
        for worker in self.workers:
            salaries += worker.salary
        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        budget_needed = 0
        for animal in self.animals:
            budget_needed += animal.money_for_care
        if self.__budget >= budget_needed:
            self.__budget -= budget_needed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [animal for animal in self.animals if animal.__class__.__name__ == "Lion"]
        tigers = [animal for animal in self.animals if animal.__class__.__name__ == "Tiger"]
        cheetahs = [animal for animal in self.animals if animal.__class__.__name__ == "Cheetah"]

        output = ""
        output += f"You have {len(self.animals)} animals\n"
        output += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            output += f"{lion.__repr__()}\n"
        output += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            output += f"{tiger.__repr__()}\n"
        output += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            output += f"{cheetah.__repr__()}\n"

        return output.rstrip()

    def workers_status(self):
        keepers = [worker for worker in self.workers if worker.__class__.__name__ == "Keeper"]
        caretakers = [worker for worker in self.workers if worker.__class__.__name__ == "Caretaker"]
        vets = [worker for worker in self.workers if worker.__class__.__name__ == "Vet"]

        output = ""
        output += f"You have {len(self.workers)} workers\n"
        output += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            output += f"{keeper.__repr__()}\n"
        output += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            output += f"{caretaker.__repr__()}\n"
        output += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            output += f"{vet.__repr__()}\n"

        return output.rstrip()
