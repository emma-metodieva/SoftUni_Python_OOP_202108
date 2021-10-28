from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        monthly_consumptions = 0
        for room in self.rooms:
            monthly_consumptions += room.monthly_consumption
        return f"Monthly consumptions: {monthly_consumptions:.2f}$."

    def pay(self):
        output = []
        for room in self.rooms:
            if room.budget >= room.monthly_consumption:
                room.budget -= room.monthly_consumption
                output.append(f"{room.family_name} paid {room.monthly_consumption:.2f}$ "
                              f"and have {room.budget:.2f}$ left.")
            else:
                self.rooms.remove(room)
                output.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
        return "\n".join(output)

    def status(self):
        output = ""
        output += f"Total population: {sum([room.members_count for room in self.rooms])}\n"
        for room in self.rooms:
            output += f"{room.family_name} with {room.members_count} members. " \
                      f"Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            if len(room.children) > 0:
                n = 0
                for child in room.children:
                    n += 1
                    output += f"--- Child {n} monthly cost: {30 * child.cost:.2f}$\n"
            output += f"--- Appliances monthly cost: {room.calculate_expenses(room.appliances):.2f}$\n"
        return output
