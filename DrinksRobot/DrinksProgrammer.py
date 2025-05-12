from RobotState import RobotState



class DrinksProgrammer:
    def __init__(self, comms, script_queue):
        self.comms = comms
        self.script_queue = script_queue
        self.program_map = {
            "CUBAVodka": "test1.urp",
            "LimeSirup": "test2.urp",
            "Cola": "test3.urp",
            "brandbil": "test1.urp",
            "rom_og_cola": "rom_og_cola.urp",

            "solstang": "solstang.urp"
        }

        self.name_mapping = {
            "CUBA Vodka": "CUBAVodka",
            "CUBA Apricot": "CUBAVodka",
            "CUBA Caramel": "CUBAVodka",
            "CUBA Strawberry": "CUBAVodka",
            "CUBA Orange": "CUBAVodka",
            "CUBA Dry Lemon": "CUBAVodka",
            "CUBA Kurant": "CUBAVodka",
            "CUBA Passion": "CUBAVodka",
            "CUBA Raspberry": "CUBAVodka",
            "CUBA Pineapple": "CUBAVodka",
            "CUBA Mango": "CUBAVodka",
            "CUBA Watermelon": "CUBAVodka",

            "BARMIX Lime Sirup": "LimeSirup",
            "BARMIX Grenadine Sirup": "LimeSirup",
            "BARMIX Curacao Sirup": "LimeSirup",
            "BARMIX Blackberry Sirup": "LimeSirup",
            "BARMIX Sugar Cane Sirup": "LimeSirup",
            "BARMIX Strawberry Sirup": "LimeSirup",
            "BARMIX Rhubarb Sirup": "LimeSirup",
            "BARMIX Mango Sirup": "LimeSirup",

            "Appelsinjuice": "Cola",
            "Ananasjuice": "Cola",
            "Æblejuice": "Cola",
            "Mangojuice": "Cola",
            "Ingefærjuice": "Cola",
            "Cola": "Cola",
            "Sprite": "Cola",
            "Hindbærbrus": "Cola",
            "Grøn sport": "Cola",
            "Fanta Appelsin": "Cola",
            "Fanta Lemon": "Cola",
            "Fanta Exotic": "Cola"

        }



    def run_program(self, drink_name):
        if drink_name in self.program_map:
            program = self.program_map[drink_name]
            print(f"Kører {drink_name} program...")
            self.queue_program(program)  # <-- Vigtigt at bruge queue_program her!

            RobotState.idle_counter = 0
            RobotState.pause_script_active = False
            print("Idle counter reset efter valg!")
        else:
            print(f"Ukendt drink navn: {drink_name}")

    def mix_drink(self, ingredients):
        RobotState.idle_counter = 0
        RobotState.pause_script_active = False
        RobotState.progress_done = 0
        RobotState.progress_total = len(ingredients) * 2
        for ingredient in ingredients:
            mapped_name = self.name_mapping.get(ingredient, None)
            if mapped_name and mapped_name in self.program_map:
                program_name = self.program_map[mapped_name]
                self.queue_program(program_name)
            else:
                print(f"Ukendt ingrediens: {ingredient}")

    def queue_program(self, program_name):
        # Hver program består af load + play kommandoer
        load_command = f'load {program_name}\n'
        play_command = 'play\n'

        # Tilføj load og play til køen
        self.script_queue.add_script(load_command)
        self.script_queue.add_script(play_command)
