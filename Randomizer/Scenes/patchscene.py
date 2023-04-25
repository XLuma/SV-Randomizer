import os
import json
import copy

sprigattio_offset = 0x3D8A #6c 02
fuecoco_offset = 0x158A #6d 02
quaxly_offset = 0x2992 #6e 02

def fetch_devname(index: int, csvdata):
    return str.strip(csvdata[index])

def fetch_devname_index(name:str, csvdata):
    for index, current_name in enumerate(csvdata):
        if str.strip(current_name) == name:
            return index


def patchIndividualScenes():
    #thats ugly but i have no inspiration rn
    scarlet_scene = open(os.getcwd() + "/Randomizer/Scenes/common_0070_always_0_clean.trsog", "rb")
    violet_scene = open(os.getcwd() + "/Randomizer/Scenes/common_0070_always_1_clean.trsog", "rb")
    scarlet_scene_bytes = scarlet_scene.read()
    violet_scene_bytes = violet_scene.read()
    scarlet_scene.close()
    violet_scene.close()

    #print(scarlet_scene_bytes)
    #thats even more ugly but f it
    with open(os.getcwd() + "/Randomizer/Scenes/common_0070_always_0.trsog", "w+b") as file:
        file.write(scarlet_scene_bytes)
        file.seek(sprigattio_offset)
        file.write(b'\x6C\x02')
        file.seek(fuecoco_offset)
        file.write(b'\x6D\x02')
        file.seek(quaxly_offset)
        file.write(b'\x6E\x02')
    with open(os.getcwd() + "/Randomizer/Scenes/common_0070_always_1.trsog", "w+b") as file:
        file.write(violet_scene_bytes)
        file.seek(sprigattio_offset)
        file.write(b'\x6C\x02')
        file.seek(fuecoco_offset)
        file.write(b'\x6D\x02')
        file.seek(quaxly_offset)
        file.write(b'\x6E\x02')

def retrieve_starter(starters, label):
    for entry in starters['values']:
        if entry['label'] == label:
            return entry

def retrieve_catalog_entry(catalog: dict, species, form, fake_catalog_index):
    for entry in catalog['unk_1']:
        if entry['speciesinfo']['species_number'] == species and entry['speciesinfo']['form_number'] == form:
            #return_entry = entry #probably unnecessary
            return_entry = copy.deepcopy(entry)
            return_entry['speciesinfo']['species_number'] = fake_catalog_index
            if form != 0:
                return_entry['speciesinfo']['form_number'] = 0
                for anim in return_entry['animations']:
                    anim['form_number'] = 0
                for locator in return_entry['locators']:
                    locator['form_number'] = 0
            return return_entry
        
def patchCatalog(names: list, catalog, starters):
    starter_array_order = ['common_0065_kusa', 'common_0065_hono', 'common_0065_mizu'] #prevents me from writing a lot of useless code
    fake_catalog_species = 620
    for current_starter in starter_array_order:
        starter = retrieve_starter(starters, current_starter)
        species_index = fetch_devname_index(starter['pokeData']['devId'], names)
        form_index = starter['pokeData']['formId']
        catalog_entry = retrieve_catalog_entry(catalog, species_index, form_index, fake_catalog_species) #replace species index
        catalog['unk_1'].append(catalog_entry)
        fake_catalog_species = fake_catalog_species + 1 #this goes until 622
    pass

def patchScenes():
    #load starters
    starterfile = open(os.getcwd() + "/Randomizer/Starters/" +"eventAddPokemon_array.json", "r") #0 is fuecoco, 1 is sprigattio, 2 is quaxly
    starters = json.load(starterfile)
    starterfile.close()

    #load model catalog
    catalogfile = open(os.getcwd() + "/Randomizer/Scenes/poke_resource_table_clean.json", "r")
    catalog = json.load(catalogfile)
    catalogfile.close()

    #load names
    file = open(os.getcwd() + "/Randomizer/Starters/" +"pokemon_to_id.txt", "r")
    names = []
    for name in file:
        names.append(name)
    file.close()

    patchIndividualScenes()
    patchCatalog(names, catalog, starters)
    
    outdata = json.dumps(catalog, indent=4)
    with open(os.getcwd() + "/Randomizer/Scenes/" +"poke_resource_table.json", 'w') as outfile:
        outfile.write(outdata)
    print("Patched starters in overworld")