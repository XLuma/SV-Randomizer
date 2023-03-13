import csv
import json
import random
import os

def fetch_devname(index: int, csvdata):
    #print(csvdata[index])
    return str.strip(csvdata[index])

def get_alt_form(index: int):
    has_alt = [26, #raichu
    50, #diglett
    51, #dugtrio
    52, #meowth, has two
    53, #persian
    58, #growlithe
    59, #arcanine
    79, #slowpoke
    80, #slowbro, seems to be form id 2
    88, #grimer
    89, #muk
    100, #voltorb
    101, #electrode
    128, #tauros, 3 form possible 1 2 3
    144, #articuno
    145, #zapdos
    146, #moltres
    157, #typhlosion
    194, #wooper
    199, #slowking
    211, #qwilfish
    215, #sneasel
    422, #shellos
    423, #gastrodon
    479, #rotom: 5 forms 0 1 2 3 4 5
    483, #dialga: force it to be origin
    484, #palkia: force it to be origin
    487, #giratina
    #fuck arceus
    503, #samurott
    549, #lilligant
    550, #basculin, form 2
    570, #zorua
    571, #zoroark
    #fuck deerling
    628, #braviary
    641, #tornadus
    642, #thundurus
    645, #landorus
    648, #meloetta
    705, #sligoo
    706, #goodra
    713, #avalugg
    720, #hoopa
    724, #decidueye
    741, #oricorio, 3 forms 0 1 2 3
    744, #rockruff
    745, #lycanroc: 2 forms 0 1 2
    849, #toctricity
    892, #urshifu
    893, #zarude
    898, #calyrex, 2 forms 0 1 2 
    ]
    if index in has_alt: #previously, we just shuffled around. Now we include all species, so we need more edge cases
        choice = 0
        match index:
            case 52:
                choice = random.randint(0, 2)
                #forms = [1, 2]
                return choice
            case 80:
                choice = random.randint(0, 100)
                if choice < 49:
                    return 2
                else:
                    return 0
            case 128:
                choice = random.randint(0, 3)
                #forms = [0,1,2,3]
                #choice = [0] #only base tauros is not present
                #form_index = form_index + 1
                return choice
            case 194:
                choice = random.randint(0, 100)
                if choice < 49:
                    return 1
                else:
                    return 0
                #return [0] #base wooper is not in the encounter table
            case 479:
                choice = random.randint(0,5)
                forms = [1,2,3,4,5]
                return choice
            case 550:
                choice = random.randint(0, 100)
                if choice < 49:
                    return 2
                else:
                    return 0
            case 745: #all forms already in the table
                 choice = random.randint(0, 2)
            #    forms = [0,1,2]
            #    choice = forms[form_index]
            #    form_index = form_index + 1
                 return choice
            case 898:
                choice = random.randint(0, 2)
                #forms = [1,2]
                return choice
            case _:
                choice = random.randint(0, 100)
                if choice < 49:
                    return 0
                else:
                    return 1
    else:
        return  0


allowed_species = [ 4, 5, 6, 25, 26, 39, 40, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 79, 80, 81, 82, 88, 89, 90, 91, 92, 93, 94, 96, 97, 100, 101, 113, 123, 128, 129, 130, 132, 133, 134, 135, 136, 144, 145, 146, 147, 148, 149, 150, 151, 155, 156, 157, 172, 174, 179, 180, 181, 183, 184, 185, 187, 188, 189, 191, 192, 194, 195, 196, 197, 198, 199, 200, 203, 204, 205, 206, 211, 212, 214, 215, 216, 217, 225, 228, 229, 231, 232, 234, 242, 246, 247, 248, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 296, 297, 298, 302, 307, 308, 316, 317, 322, 323, 324, 325, 326, 331, 332, 333, 334, 335, 336, 339, 340, 353, 354, 357, 361, 362, 370, 371, 372, 373, 382, 383, 384, 396, 397, 398, 401, 402, 403, 404, 405, 415, 416, 417, 418, 419, 422, 423, 425, 426, 429, 430, 434, 435, 436, 437, 438, 440, 442, 443, 444, 445, 447, 448, 449, 450, 453, 454, 456, 457, 459, 460, 461, 462, 470, 471, 475, 478, 479, 480, 481, 482, 483, 484, 485, 487, 488, 493, 501, 502, 503, 548, 549, 550, 551, 552, 553, 570, 571, 574, 575, 576, 585, 586, 590, 591, 594, 602, 603, 604, 610, 611, 612, 613, 614, 615, 624, 625, 627, 628, 633, 634, 635, 636, 637, 641, 642, 645, 648, 650, 651, 652, 653, 654, 655, 656, 657, 658, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 690, 691, 692, 693, 700, 701, 702, 703, 704, 705, 706, 707, 712, 713, 714, 715, 719, 720, 721, 722, 723, 724, 734, 735, 739, 740, 741, 744, 745, 747, 748, 749, 750, 753, 754, 757, 758, 761, 762, 763, 765, 766, 769, 770, 775, 778, 779, 801, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 833, 834, 837, 838, 839, 840, 841, 842, 843, 844, 846, 847, 848, 849, 854, 855, 856, 857, 858, 859, 860, 861, 863, 870, 871, 872, 873, 874, 875, 876, 878, 879, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]
tera_types = ['normal','kakutou', 'hikou', 'doku', 'jimen', 'iwa', 'mushi', 'ghost', 'hagane', 'honoo', 'mizu', 'kusa', 'denki', 'esper', 'koori', 'dragon', 'aku', 'fairy']
def check_important_trainer(id: str):
    prefixes = ['leader', 'chair', "e4"]
    for prefix in prefixes:
        if prefix in id:
            return True
    return False

average_level = 0
def make_poke(pokeEntry, index: str, csvdata, config):
    if config['force_6_pokemons_on_important_trainers'] == 'yes' and check_important_trainer(pokeEntry['trid']) == True:
        chosenmon = allowed_species[random.randint(0, 475)]
        pokeEntry['poke' + index]['devId'] = fetch_devname(chosenmon, csvdata)
        pokeEntry['poke' + index]['formId'] = get_alt_form(chosenmon)
        pokeEntry['poke' + index]['sex'] = "DEFAULT"
        pokeEntry['poke' + index]['level'] = pokeEntry['poke1']['level']
        if (random.randint(0, 100) < 50):
            pokeEntry['poke' + index]['level'] = pokeEntry['poke' + index]['level'] + 1
        pokeEntry['poke' + index]['wazaType'] = "DEFAULT"
        pokeEntry['poke' + index]['waza1']['wazaId'] = "WAZA_NULL"
        pokeEntry['poke' + index]['waza2']['wazaId'] = "WAZA_NULL"
        pokeEntry['poke' + index]['waza3']['wazaId'] = "WAZA_NULL"
        pokeEntry['poke' + index]['waza4']['wazaId'] = "WAZA_NULL" #6 mons on gyms, elite 4 champ
        if config['force_perfect_ivs'] == "yes":
            talentvalue = {
                "hp": 31,
                "atk": 31,
                "def": 31,
                "spAtk": 31,
                "spDef": 31,
                "agi": 31
            }
            pokeEntry['poke' + index]['talentValue'] = talentvalue
        if config['randomize_fixed_tera_type'] == "yes" and pokeEntry['poke' + index]['gemType'] != "DEFAULT":
            pokeEntry['poke' + index]['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()
        if config['randomize_all_tera_type'] == "yes":
            pokeEntry['poke' + index]['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()
    else:  
        if pokeEntry['poke' + index]['devId'] != "DEV_NULL":   
            chosenmon = allowed_species[random.randint(0, 475)]
            pokeEntry['poke' + index]['devId'] = fetch_devname(chosenmon, csvdata)
            pokeEntry['poke' + index]['formId'] = get_alt_form(chosenmon)
            pokeEntry['poke' + index]['wazaType'] = "DEFAULT"
            pokeEntry['poke' + index]['waza1']['wazaId'] = "WAZA_NULL"
            pokeEntry['poke' + index]['waza2']['wazaId'] = "WAZA_NULL"
            pokeEntry['poke' + index]['waza3']['wazaId'] = "WAZA_NULL"
            pokeEntry['poke' + index]['waza4']['wazaId'] = "WAZA_NULL"
            if config['force_perfect_ivs'] == "yes":
                talentValue = {
                    "hp": 31,
                    "atk": 31,
                    "def": 31,
                    "spAtk": 31,
                    "spDef": 31,
                    "agi": 31
                }
                pokeEntry['poke' + index]['talentValue'] = talentValue
            if config['randomize_fixed_tera_type'] == "yes" and pokeEntry['poke' + index]['gemType'] != "DEFAULT":
                pokeEntry['poke' + index]['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()
            if config['randomize_all_tera_type'] == "yes":
                pokeEntry['poke' + index]['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()

def randomize(config):
    #load information
    file = open(os.getcwd() + "/Randomizer/Trainers/" +"trdata_array_clean.json", "r")
    data = json.load(file)

    csvfile = open(os.getcwd() + "/Randomizer/Trainers/" +"pokemon_to_id.txt", "r")
    csvdata = []
    for i in csvfile:
        csvdata.append(i)
    csvfile.close()

    for entry in data['values']:
        i = 1

        while i < 7:
            make_poke(entry, str(i), csvdata, config)
            i = i + 1
        if config['make_ai_smart_for_all_trainers'] == "yes":
            entry['aiBasic'] = True
            entry['aiHigh'] = True
            entry['aiExpert'] = True
            entry['aiChange'] = True
        if config['allow_all_trainers_to_terastalize'] == "yes":
            entry['changeGem'] = True

    outdata = json.dumps(data, indent=4)
    with open(os.getcwd() + "/Randomizer/Trainers/" +"trdata_array.json", 'w') as outfile:
        outfile.write(outdata)
    print("Randomisation done !")

def main():
   randomize()

if __name__ == "__main__":
    main()
