class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [room for room in self.rooms if room.number == room_number]
        if len(room) > 0:
            result = room[0].take_room(people)
            if result is None:
                self.guests += people

    def free_room(self, room_number):
        room = [room for room in self.rooms if room.number == room_number]
        if len(room) > 0:
            self.guests -= room[0].guests
            room[0].free_room()

    def status(self):
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]

        return f"Hotel {self.name} has {self.guests} total guests" \
               f"\nFree rooms: {', '.join(free_rooms)}" \
               f"\nTaken rooms: {', '.join(taken_rooms)}"
