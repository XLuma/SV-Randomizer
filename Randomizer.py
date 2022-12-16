import json
import os
import Randomizer.WildEncounters.wildrando as WildRandomizer
import Randomizer.Trainers.trainerrando as TrainerRandomizer
import Randomizer.PersonalData.personal_randomizer as PersonalRandomizer
import Randomizer.Starters.randomize_starters as StarterRandomizer
import Randomizer.StaticSpawns.statics as StaticRandomizer
import shutil
import subprocess
import platform

#thanks zadenowen for the function
def generateBinary(schema: str, json: str, path: str):
    iswindows = platform.system() == "Windows"
    flatc = os.path.abspath("flatc/flatc.exe") if iswindows else "flatc"  # works for me, won't work if you don't have flatc installed, probably works on mac
    outpath = os.path.abspath("output/romfs/" + path)
    print(outpath)
    proc = subprocess.run(
        [flatc,
        "-b",
        "-o",
        outpath,
        os.path.abspath(schema),
        os.path.abspath(json)
        ], capture_output=True
    )
    return proc

def open_config():
    file = open("config.json", "r")
    config = json.load(file)
    file.close()
    return config

def create_modpack():
    if os.access("output/romfs", mode=777) == True: #exists
        shutil.rmtree("output/romfs")
    os.makedirs("output/romfs", mode=777, exist_ok=True)

paths = {
    "wilds": "world/data/encount/pokedata/pokedata",
    "trainers": "world/data/trainer/trdata",
    "gifts": "world/data/event/event_add_pokemon/eventAddPokemon",
    "personal": "avalon/data",
    "statics": "world/data/field/fixed_symbol/fixed_symbol_table",
    "tms": "world/data/item/itemdata"
}
def randomize():
    config = open_config()
    create_modpack()
    if config['wild_randomizer']['is_enabled'] == "yes":
        WildRandomizer.randomize(config['wild_randomizer'])
        generateBinary("Randomizer/WildEncounters/pokedata_array.bfbs", "Randomizer/WildEncounters/pokedata_array.json", paths["wilds"])
    if config['trainer_randomizer']['is_enabled'] == "yes":
        TrainerRandomizer.randomize(config['trainer_randomizer'])
        generateBinary("Randomizer/Trainers/trdata_array.bfbs", "Randomizer/Trainers/trdata_array.json", paths["trainers"])
    if config['personal_data_randomizer']['is_enabled'] == "yes":
        PersonalRandomizer.randomize(config['personal_data_randomizer'])
        generateBinary("Randomizer/PersonalData/personal_array.fbs", "Randomizer/PersonalData/personal_array.json", paths["personal"])
    if config['starter_randomizer']['is_enabled'] == "yes":
        StarterRandomizer.randomize(config['starter_randomizer'])
        generateBinary("Randomizer/Starters/eventAddPokemon_array.bfbs", "Randomizer/Starters/eventAddPokemon_array.json", paths["gifts"])
    if config['static_randomizer']['is_enabled'] == "yes":
        StaticRandomizer.randomize(config['static_randomizer'])
        generateBinary("Randomizer/StaticSpawns/fixed_symbol_table_array.bfbs", "Randomizer/StaticSpawns/fixed_symbol_table_array.json", paths["statics"])
    shutil.make_archive("output/randomizer", "zip", "output/romfs/")

def test():
    create_modpack()

def main():
    randomize()
if __name__ == "__main__":
    main()
