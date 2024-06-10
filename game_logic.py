import random
from room import Room
from character import Character
from enemy import Enemy
from ascii_art import AsciiArt
from remove_diacritics import DiacriticRemover



class GameLogic:
    def __init__(self):
        self.setup_rooms()
        self.player = Character("Väzeň")
        self.current_room = self.dungeon  # hráč začína v temnici
        self.enemy_appeared = False
        self.hidden_chamber_unlocked = False 
        self.gates_to_hell_visited = False
        AsciiArt.show_art1()

    def setup_rooms(self):
        self.rooms = []
        self.pouzite_rooms = []
        self.prazdne_rooms = []

        direction_to_forest_walkway = "sever" if random.choice([True, False]) else "juh"

        # Define the rooms
        self.castle = Room("Hrad", "Nachádzaš sa vo Velkolepom hrade s vysokými vežami a veľkou bránou.")
        self.dungeon = Room("Temnica", "Zobúdzaš sa v tmavej, vlhkej temnici so strašným zápachom. Nikoho okolo nevidíš a nespomínaš si, čo sa ti stalo.")
        self.tower = Room("Veža", "Vysoká veža s výhľadom na okolie hradu. Svojim pohľadom taktiež vidíš hrad a nádvorie pod tebou. Na veži veje vlajka Rodiny Dračích Strážcov.")
        self.courtyard = Room("Nádvorie", "Veľké nádvorie s trávou a kamennými stĺpmi. Pohľadom okolo toto miesto spoznávaš. Je to predsa 'Hrad Strážný Prameň'.")
        self.forest = Room("Les", "Hustý les s vysokými stromami a zvukmi divočiny. Počas toho, ako vchádzaš do lesa, vidíš v pni zaseknutú sekeru. Nad lesom je dym z ohniska, ktoré musí byť neďaleko.")
        self.fireplace = Room("Ohnisko pri križovatke", "Ako pomaly pristupuješ k ohnisku, vidíš, že už je vyhasnuté, no cítiš vôňu spáleného mäsa. Nad ohniskom sa nachádza skalka a za ohniskom vidíš rozdelenú cestu.")
        self.forest_walkway = Room("Lesný priechod", "Už si trochu ďalej od ohniska a puch spáleného mäsa mizne. Ty sa však prechádzaš po lesnej cestičke a ostávaš v pozore. Nikdy nevieš, čo na teba vybehne.")
        self.skalisko = Room("Skalisko", "Horko-ťažko si sa vyšplhal na skalisko. Cestou, z ktorej si prišiel, sa už vrátiť nedokážeš. No možno by si vedel zliesť k ohnisku. Nad týmto miestom s krásnym výhľadom je však cítiť niečo nedobré.")
        self.library = Room("Knižnica", "Starodávna knižnica plná starých zvitkov a kníh, kde sa ukrývajú pradávne vedomosti.")
        self.armory = Room("Zbrojnica", "Miestnosť plná zbraní a brnení, kde sa môžeš vybaviť na ďalšie dobrodružstvá.")
        self.hidden_chamber = Room("Skrytá komnata", "Tajná miestnosť, ktorá je skrytá za posuvnou stenou. V jej strede stojí starobylý oltár.")
        self.crypt = Room("Krypta", "Tmavá a chladná krypta, kde sú pochovaní dávni hrdinovia a šľachtici.")
        self.garden = Room("Záhrada", "Pokojná záhrada plná kvetov a fontán, konečne tu cítiš mier a kľud.")
        self.cave = Room("Jaskyňa", "Temná jaskyňa s tajomnými priekopami a úkrytmi. Ako precházdaš jaskyňou cítiš úskosť pocit niečoho nekalého. Možno by sa mal vrátiť kým to ešte dokážeš.")
        self.hell_gate = Room("Pekelné brány", "Už niet cesty späť. Vydíš pred sebebou pekelné brány a vieš že už niet cesty späť. Krokom vpred sa tvoja nočná mora možno skončí. Toto je tvoje posledné útočisko.")
        self.hell = Room("Peklo", "Vstupuješ do temného a horúceho miesta. Okolo teba sú plamene a počuješ zúfalé výkriky duší, ktoré tu trpia. Vzduch je ťažký a horúci, a cítiš, ako sa tvoja koža napína od tepla. Pred tebou sa objavuje \033[31;1;6mdémon\033[0m, ktorý je strážcom tohto miesta. Toto je tvoj posledný boj, miesto, kde sa rozhodne o tvojom osude. Vložil si do toho všetko čo si mohol?")



        # List všetkých miestností
        self.rooms.extend([self.castle, self.dungeon, self.tower, self.courtyard, self.forest, self.fireplace,
                           self.forest_walkway, self.skalisko, self.library, self.armory, self.hidden_chamber,
                           self.crypt, self.garden, self.cave, self.hell_gate, self.hell])

        random.shuffle(self.rooms)  # náhodné umiestnenie miestností

        # Prepojenie
        self.castle.link_room(self.dungeon, "dole")
        self.castle.link_room(self.tower, "hore")
        self.castle.link_room(self.courtyard, "vychod")
        self.castle.link_room(self.library, "sever")
        self.dungeon.link_room(self.castle, "hore")
        self.dungeon.link_room(self.crypt, "juh")
        self.tower.link_room(self.castle, "dole")
        self.courtyard.link_room(self.castle, "zapad")
        self.courtyard.link_room(self.forest, "vychod")
        self.courtyard.link_room(self.garden, "juh")
        self.forest.link_room(self.courtyard, "zapad")
        self.forest.link_room(self.fireplace, "vychod")
        self.fireplace.link_room(self.forest, "zapad")
        self.fireplace.link_room(self.forest_walkway, direction_to_forest_walkway)
        self.forest_walkway.link_room(self.fireplace, "juh" if direction_to_forest_walkway == "sever" else "sever")
        self.forest_walkway.link_room(self.skalisko, "hore")
        self.skalisko.link_room(self.fireplace, "dole")
        self.library.link_room(self.castle, "juh")
        self.library.link_room(self.armory, "vychod")
        self.armory.link_room(self.library, "zapad")
        #self.armory.link_room(self.hidden_chamber, "dole")
        self.hidden_chamber.link_room(self.armory, "hore")
        self.hidden_chamber.link_room(self.cave, "juh")
        self.crypt.link_room(self.dungeon, "sever")
        self.garden.link_room(self.courtyard, "sever")
        self.cave.link_room(self.hidden_chamber, "sever")
        self.cave.link_room(self.hell_gate, "juh")
        self.hell_gate.link_room(self.hell, "dole")


        # Náhodné uniestnenie predmetov
        items = ["Meč", "Štít", "Lektvar zdravia", "Lektvar zdravia", "Helma", "Starodávna kniha", "Magický amulet", "Elixír sily"]

        self.prazdne_rooms = [self.crypt,self.cave,self.hell_gate,self.hidden_chamber,self.hell]

        for item in items:
            room = random.choice(self.rooms)  # náhodný výber miestnosti
            while room in self.prazdne_rooms:
                room = random.choice(self.rooms)  # 
            room.add_item(item)

        # Pridanie špecifických itemov
        self.forest.add_item("Sekera")
        self.garden.add_item("Lúčna kvetina")
        if random.randint(0,99) < 50:
            self.hell_gate.add_item("Lektvar zdravia")

        # PRIDAVANIE ENEMMIES
        self.pouzite_rooms = [self.dungeon,self.garden,self.hell_gate]
        self.pouzite_rooms.append(self.dungeon)
        self.pouzite_rooms.append(self.garden)

        enemies = [
            ("Matka medvedica", 9, 6, self.skalisko),
            ("Obhorený kostlivec", 8, 5, self.fireplace),
            ("Strážca knižnice", 7, 3, self.library),
            ("Mŕtvy strážny", 6, 4, self.cave),
            ("Železný rytier", 10, 5, self.armory),
            ("Ghúl", 14, 5, self.crypt),
            ("Démon", 20, 10, self.hell),
            ("Mŕtvy strážny", 5, 4, random.choice(self.rooms)),
            ("Potkan", 2, 2, random.choice(self.rooms))
            

        ]

        for name, hp, damage, room in enemies:
            while room in self.pouzite_rooms:
                room = random.choice(self.rooms)
            enemy = Enemy(name, hp, damage)
            room.enemy = enemy
            self.pouzite_rooms.append(room)

        


    def show_options(self):
        print("\n\033[1mMožnosti:")
        print("   1. Štart")
        print("   2. Pozrieť príkazy")
        print("   3. Zmeniť meno")
        print("   4. Koniec\033[0m")

    def show_commands(self):
        print("\nPríkazy:")
        print("- 'pozri prikazy' pre zobrazenie tohto listu príkazov")
        print("- Zadaj smer \033[36m(sever, juh, východ, západ, hore, dole)\033[0m pre presun z miestnosti")
        print("- 'vezmi \033[33m[predmet]\033[0m'")
        print("- 'inventár' pre zobrazenie predmetov aj s popiskom")
        print("- 'bojuj' pre útok na nepriateľa")
        print("- 'použi (napríklad lektvar zdravia alebo ine) pre pouzitie predmetu")
        print("- 'koniec' pre ukončenie hry")
    
    def use_item(self, item_name, hp_increase=0, max_hp_check=True, special_action=None):
        if item_name in self.player.inventory:
            if not max_hp_check or self.player.hp < self.player.max_hp:  
                if hp_increase > 0:
                    self.player.hp += hp_increase
                    if self.player.hp > self.player.max_hp:
                        self.player.hp = self.player.max_hp
                self.player.inventory.remove(item_name)
                if special_action:
                    special_action()
                else:
                    print(f"\033[32mPoužil si {item_name} a obnovil si si {hp_increase} HP.\033[0m")
            else:
                print(f"\033[32mMáš maximálne zdravie, nemôžeš použiť {item_name}.\033[0m")
        else:
            print(f"\033[45mNemáš žiadny {item_name}.\033[0m")

    def special_action_key(self):
        if self.current_room == self.armory:
            if not self.hidden_chamber_unlocked:
                print("\033[32mPoužil si Tajomný klúč a odomkol si cestu do skrytej komory.\033[0m")
                self.hidden_chamber_unlocked = True
                self.armory.link_room(self.hidden_chamber, "dole")
            else:
                print("\033[33mCesta do skrytej komory je už odomknutá.\033[0m")
        else:
            print("\033[31mTajomný klúč sa tu nedá použiť.\033[0m")

    def special_action_book(self):
        print("\033[32mOtvoril si Starodávnu knihu a začal si čítať...\033[0m")
        print("\033[34m\"V dávnych dobách, len tí najodvážnejší bojovníci vedeli o tajomstve zbrojnice. \"\033[0m")
        print("\033[34m\"Ak máš odvahu a múdrosť, nájdeš cestu do pekla tým, že použiješ Tajomný klúč v zbrojnici.\"\"\033[0m")


    def play(self):
        while self.player.is_alive():
            self.show_options()
            choice = input("Vyber možnosť: ").strip().lower()
            if choice == "1" or choice == "štart":
                AsciiArt.show_art3()
                break
            elif choice == "2" or choice == "pozrieť príkazy":
                self.show_commands()
            elif choice == "3" or choice == "zmeniť meno":
                self.player.change_name()
            elif choice == "4" or choice == "koniec":
                print("\033[45m------------------------------------- Hra ukončená -------------------------------------\033[0m")
                AsciiArt.show_art2()
                return
            else:
                print("\033[31m-----------Neplatná voľba. Prosím, vyber jednu z uvedených možností.-----------\033[0m")

        while self.player.is_alive():
            if self.current_room == self.hell_gate and self.gates_to_hell_visited == False:
                AsciiArt.show_art5()
                self.gates_to_hell_visited == True
            self.current_room.get_details()

            print("\nZadaj príkaz alebo \033[36m'pozri príkazy'\033[0m pre zoznam všetkých príkazov.")
            command = input("Tvoj príkaz:  \033[33m").strip().lower()
            command = DiacriticRemover().remove_diacritics(command)
            print("\033[0m\n\033[44m----------------------------------------------------------------------------------------\033[0m\n\n")
            print("\033[44m----------------------------------------------------------------------------------------\033[0m\n")
            
            if self.current_room.enemy and self.player.is_alive() and command != "pozri prikazy":
                print(f"\033[31m\n-----------Nepriateľ vás napadol: {self.current_room.enemy.name}.-----------\033[0m")
                enemy_damage = self.current_room.enemy.attack()
                print(f"\033[31m{self.current_room.enemy.name} zasadil vám \033[6m{enemy_damage}\033[25m poškodenie.\033[0m")
                self.player.take_damage(enemy_damage)
                if not self.player.is_alive():
                    print("\033[41;6mHra skončila, nepriateľ vás porazil.\033[0m")
                    AsciiArt.show_art2()
                    break

            if command == "koniec" or command == 'k':
                print("\033[45;6m------------------------------------- Hra ukončená -------------------------------------\033[0m")
                               
                AsciiArt.show_art2()
                break

            elif command == "pozri prikazy":
                self.show_commands()

            elif command == "bojuj":
                if self.current_room.enemy and self.player.is_alive():
                    print(f"\033[32mTvoje aktuálne HP: \033[6m{self.player.hp}/{self.player.max_hp}\033[0m")
                    enemy_damage = self.current_room.enemy.attack()
                    if "Meč" in self.player.inventory:
                        player_damage = random.randint(0, 4)
                        player_damage = player_damage + 1
                    elif "Sekera" in self.player.inventory:
                        player_damage = random.randint(0, 6)
                    else:
                        player_damage = random.randint(0, 4)
                    
                    if self.player.strength_potion_active:
                        player_damage += 4
                        self.player.end_turn()


                    if "Magický amulet" in self.player.inventory:
                        if random.randint(0,99) < 20:
                            print(f"\033[32mDal si critical (sila tvojho utoku sa zdvojnáslobila)\033[0m")
                            player_damage = player_damage * 2

                    self.current_room.enemy.take_damage(player_damage)
                    print(f"\033[32mZasadil si nepriateľovi \033[6m{player_damage}\033[25m poškodenie.\033[0m")
                    if not self.current_room.enemy.is_alive():
                        if random.randint(0,99) < 22:
                            self.current_room.add_item("Občerstvenie")
                        if self.current_room.enemy.name == "Obhorený kostlivec":
                            self.current_room.add_item("Použitá zbroj")
                        if self.current_room.enemy.name == "Železný rytier":
                            self.current_room.add_item("Kvalitná zbroj")
                        if self.current_room.enemy.name ==  "Ghúl":
                            self.current_room.add_item("Tajomný klúč")
                        if self.current_room.enemy.name ==  "Matka medvedica":
                            self.current_room.add_item("Plášť z medveďa")
                            self.current_room.add_item("Občerstvenie")
                        if self.current_room.enemy.name ==  "Démon":
                            print("\n\033[31;1m Démon je mŕtvy, no ty si však opustený v pekle. Zúfalé výkriky duší, ktoré tu trpia stále cítiš no veríš to že tvoja obeta zachránila duše ľudí z královstva. Možno sa stadiaľto vieš dostať no ty však nevieš ako.\n")
                            AsciiArt.show_art4()
                            break
                        #print(f"\033[32mZabil si nepriateľa: {self.current_room.enemy.name}.\033[0m")
                        self.current_room.enemy = None
                else:
                    print("\n\033[45m-------------------------------- Nemáš na koho zaútočiť --------------------------------\033[0m")
                                     
            elif command.startswith("vezmi "):
                item_name = command.split(" ", 1)[1]
                found_item = None
                for item in self.current_room.items:
                    if DiacriticRemover().remove_diacritics(item.lower()) == item_name:
                        found_item = item
                        break
                if found_item:
                    if found_item == "Helma":
                        self.player.pick_up(found_item)
                        self.player.increase_max_hp(1)
                        print("Vzal si \033[33;3mhelmu\033[0m a \033[32mtvoje maximálne HP bolo zvýšené o 1.\033[0m")
                    elif found_item == "Štít":
                        self.player.pick_up(found_item)
                        self.player.increase_max_hp(2)
                        print("Vzal si \033[33;3mštít\033[0m a \033[32mtvoje maximálne HP bolo zvýšené o 2.\033[0m")
                    elif found_item == "Plášť z medveďa":
                        self.player.pick_up(found_item)
                        self.player.increase_max_hp(2)
                        print("Vzal si \033[33;3mPlášť z medveďa\033[0m a \033[32mtvoje maximálne HP bolo zvýšené o 2.\033[0m")
                    elif found_item == "Použitá zbroj":
                        if "Kvalitná zbroj" in self.player.inventory:
                            print("Rozhodol si sa ponechať si \033[33;3mkvalitnú zbroj\033[0m a zahodil si použitú.")
                            self.player.inventory.remove("Použitá zbroj")
                            self.player.increase_max_hp(-2)
                        self.player.pick_up(found_item)
                        self.player.increase_max_hp(2)
                        print("Obliekol si si \033[33;3mpoužitú zbroj\033[0m \033[32mtvoje maximálne HP bolo zvýšené o 2.\033[0m")
                    elif found_item == "Kvalitná zbroj":
                        if "Použitá zbroj" in self.player.inventory:
                            print("Vzal si si \033[33;3mKvalitnú zbroj\033[0m a zahodil si použitú.")
                            self.player.inventory.remove("Použitá zbroj")
                            self.player.increase_max_hp(-2)
                        self.player.pick_up(found_item)
                        self.player.increase_max_hp(3)
                        print("Obliekol si si \033[33;3mKvalitnú zbroj\033[0m \033[32mtvoje maximálne HP bolo zvýšené o 3.\033[0m")
                    elif found_item == "Sekera" and "Meč" in self.player.inventory or found_item == "Meč" and "Sekera" in self.player.inventory:
                        replace_sword = input("Nemôžeš mať v rukách dve zbrane. Chceš si nechať \033[33mmeč\033[0m alebo \033[33msekeru\033[0m (\033[32mMeč\033[0m/\033[31mSekera\033[0m): ").strip().lower()
                        if DiacriticRemover().remove_diacritics(replace_sword) == "sekera":
                            self.player.pick_up(found_item)
                            self.player.inventory.remove("Meč")
                            print("Vzal si \033[33;3msekeru\033[0m a zahodil si meč.")
                        elif DiacriticRemover().remove_diacritics(replace_sword) == "mec":
                            self.player.pick_up(found_item)
                            self.player.inventory.remove("Sekera")
                            print("Vzal si \033[33;3mmeč\033[0m a zahodil si sekeru.")
                    else:
                        self.player.pick_up(found_item)
                        print(f"Vzal si \033[33;3m{found_item}\033[0m.")
                    self.current_room.items.remove(found_item)
                else:
                    print(f"\033[45m-------------------------------- {item_name} tu nie je --------------------------------\033[0m")
                                    
            elif command == "inventar":
                self.player.show_inventory()
            elif command.startswith("pouzi "):
                item = command.split(" ", 1)[1]
                if item == "tajomny kluc":
                    self.use_item( "Tajomný klúč", special_action=self.special_action_key,  max_hp_check=False)
                elif item == "starodavna kniha":
                    self.use_item( "Starodávna kniha", special_action=self.special_action_book, max_hp_check=False)
                elif item == "lektvar zdravia":
                    self.use_item( "Lektvar zdravia", hp_increase=5)
                elif item == "obcerstvenie":
                    self.use_item( "Občerstvenie", hp_increase=random.randint(1, 4))
                elif item == "lucna kvetina":
                    self.use_item( "Lúčna kvetina", hp_increase=3)
                elif item == "elixir sily":
                    self.use_item( "Elixír sily", special_action=self.player.use_strength_potion , max_hp_check=False)
            else:
                self.current_room = self.current_room.move(command)
            

            


