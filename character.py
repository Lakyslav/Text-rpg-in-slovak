class Character:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.hp = 10  # Začiatočné HP hráča
        self.max_hp = 10  # Maximálne HP hráča
        self.is_alive_status = True
        self.strength_potion_active = False # Kontrola či je elixir aktivny
        self.strength_potion_turns_left = 0 # Počet kôl kedy elixir funguje

    def pick_up(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        item_descriptions = {
            "Meč": "Mierne žvýši silu tvojho útoku, nedokážeš sa pomocou neho netrafiť",
            "Sekera":"Silná zbraň, má však väčšiu šancu netrafiť sa",
            "Štít": "Zvyšuje tvoju ochranu o 2",
            "Lektvar zdravia": "Obnovuje 5 životov",
            "Helma": "Zväčšuje tvoju ochranu o 1",
            "Starodávna kniha": "Aj keď je táto kniha stará a na pocit by sa kedykoľvek mohla rozpadnúť, jej použitie môže odhaliť mnohé tajomstvá",
            "Magický amulet": "20% šanca na critical útok ktoý zdvojnásobý tvoje poškodenie", 
            "Použitá zbroj":"Táto zbroj už čo to zažila, no stále zväčšuje tvoju ochranu o 2",
            "Kvalitná zbroj":"Kus kvalitnej zbroje jedené poškodenie na zbroji si spôsobil ty, zväčšuje tvoju ochranu 0 3",
            "Občerstvenie":"Môžeš použiť a ziesť aby si si obnovil HP",
            "Elixír sily":"Zvýši silu útokov na 3 kolá po použití",                        
            "Lúčna kvetina":"Voňavá kvetina z lúky, ktorá má liečivé účinky.", 
            "Tajomný klúč":"Jeho použitie v správnej miestnosti môže odhaliť spôsob na vyriešenie tejto celej situácie", 
            "Plášť z medveďa":"Tento plášť si získal výhrou nad Medvedivou, Zväčšuje tvoju ochranu o 2"
        }
        
        print(f"\033[32mTvoje aktuálne HP: \033[6m{self.hp}/{self.max_hp}\033[0m") 
        if self.inventory:
            print(f"\033[32mInventár dobrodruha {self.name}:\033[0m")
            for item in self.inventory:
                description = item_descriptions.get(item, "Bez popisu")
                print(f"\033[33m    - {item}:\033[32m {description}\033[0m")
        else:
            print("\033[32m\n-----------V inventári nemáš žiadne predmety.-----------\033[0m")


    def change_name(self):
        new_name = input("Ako sa voláš, dobrodruh?: ")
        self.name = new_name

    def is_alive(self):  # Funkcia pre kontrolu života
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.is_alive_status = False

    def increase_max_hp(self, amount):
        self.max_hp += amount
        self.hp = min(self.hp + amount, self.max_hp)

    def use_strength_potion(self):
        self.strength_potion_active = True
        self.strength_potion_turns_left = 3
        print("Použil si Elixír sily! Tvoje útoky budú silnejšie na 3 kolá.")

    def end_turn(self):
        if self.strength_potion_active:
            self.strength_potion_turns_left -= 1
            if self.strength_potion_turns_left <= 0:
                self.strength_potion_active = False
                print("Účinky Elixíru sily vypršali.")