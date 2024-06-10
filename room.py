class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.linked_rooms = {}
        self.items = []
        self.enemy = None 

    def link_room(self, room, direction):
        self.linked_rooms[direction] = room

    def add_item(self, item):
        self.items.append(item)

    def get_details(self):
        print(f"\n\033[35;1m  Miestnosť:\033[0m {self.name}")
        print(f"\033[35;1m  Popis:\033[0m \033[3;1m{self.description}\033[0m")
        print(f"\033[35;1m  Miestnosťi v okolí:\033[0m")
        for direction, room in self.linked_rooms.items():
            print(f"\033[35;1m      -\033[0m {room.name} je \033[36m{direction}\033[0m")
        if self.items:
            print("\033[35;1m   Vidíš nasledujúce predmety:\033[0m")
            for item in self.items:
                print(f"\033[33;3m      - {item}\033[0m")
        if self.enemy:
            print(f"\033[31mV miestnosti je nepriateľ: {self.enemy.name}.\033[0m")

    def move(self, direction):
        if self.enemy and self.enemy.is_alive():  # Kontrola, či je v miestnosti nepriateľ a ešte žije
            print("\033[45m-----------Nemôžeš odísť, kým je nepriateľ ešte nažive!-----------\033[0m")
            return self
        elif direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("\033[45m-----------Nesprávny príkaz!-----------\033[0m")
            return self
