class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        output = ""
        output += f"Name: {self.name}\n"
        output += f"Guild: {self.guild}\n"
        output += f"HP: {self.hp}\n"
        output += f"MP: {self.mp}\n"
        for skill_name, mana_cost in self.skills.items():
            output += f"==={skill_name} - {mana_cost}"
        output += f"\n"
        return output
