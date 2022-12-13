import json
import random
import os
allowed_moves = [1, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 97, 98, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 113, 114, 115, 116, 118, 120, 122, 123, 124, 126, 127, 129, 133, 135, 136, 137, 138, 139, 141, 143, 144, 147, 150, 151, 152, 153, 154, 156, 157, 161, 162, 163, 164, 165, 168, 172, 173, 174, 175, 178, 179, 180, 181, 182, 183, 184, 186, 187, 188, 189, 191, 192, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 217, 219, 220, 223, 224, 225, 226, 227, 229, 230, 231, 232, 234, 235, 236, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 259, 260, 261, 262, 263, 264, 266, 268, 269, 270, 271, 272, 273, 275, 276, 278, 280, 281, 282, 283, 284, 285, 286, 291, 292, 297, 298, 299, 303, 304, 305, 306, 307, 308, 309, 310, 311, 313, 314, 315, 317, 319, 321, 322, 323, 325, 326, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 347, 348, 349, 350, 351, 352, 355, 356, 359, 360, 361, 362, 364, 365, 366, 367, 368, 369, 370, 371, 372, 374, 379, 380, 383, 384, 385, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 427, 428, 430, 432, 433, 434, 435, 436, 437, 438, 440, 441, 442, 444, 446, 447, 449, 450, 451, 452, 453, 454, 455, 457, 458, 459, 460, 461, 463, 467, 468, 469, 470, 471, 472, 473, 474, 476, 478, 479, 482, 483, 484, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 499, 500, 501, 502, 503, 504, 505, 506, 508, 509, 510, 511, 512, 513, 514, 515, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 532, 533, 534, 535, 538, 539, 540, 541, 542, 547, 552, 555, 556, 557, 560, 562, 564, 565, 566, 568, 570, 572, 573, 574, 575, 577, 580, 581, 583, 584, 585, 586, 587, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 618, 619, 620, 621, 659, 660, 661, 662, 663, 665, 667, 668, 669, 670, 675, 676, 678, 679, 680, 681, 682, 683, 684, 686, 688, 689, 693, 694, 705, 706, 707, 709, 710, 715, 716, 744, 745, 746, 747, 748, 749, 750, 751, 752, 756, 776, 778, 780, 781, 782, 784, 785, 786, 787, 788, 789, 791, 793, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900]
# abilities are any number between 1 and 298, inclusive
allowed_species = [ 4, 5, 6, 25, 26, 39, 40, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 79, 80, 81, 82, 88, 89, 90, 91, 92, 93, 94, 96, 97, 100, 101, 113, 123, 128, 129, 130, 132, 133, 134, 135, 136, 144, 145, 146, 147, 148, 149, 150, 151, 155, 156, 157, 172, 174, 179, 180, 181, 183, 184, 185, 187, 188, 189, 191, 192, 194, 195, 196, 197, 198, 199, 200, 203, 204, 205, 206, 211, 212, 214, 215, 216, 217, 225, 228, 229, 231, 232, 234, 242, 246, 247, 248, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 296, 297, 298, 302, 307, 308, 316, 317, 322, 323, 324, 325, 326, 331, 332, 333, 334, 335, 336, 339, 340, 353, 354, 357, 361, 362, 370, 371, 372, 373, 382, 383, 384, 396, 397, 398, 401, 402, 403, 404, 405, 415, 416, 417, 418, 419, 422, 423, 425, 426, 429, 430, 434, 435, 436, 437, 438, 440, 442, 443, 444, 445, 447, 448, 449, 450, 453, 454, 456, 457, 459, 460, 461, 462, 470, 471, 475, 478, 479, 480, 481, 482, 483, 484, 485, 487, 488, 493, 501, 502, 503, 548, 549, 550, 551, 552, 553, 570, 571, 574, 575, 576, 585, 586, 590, 591, 594, 602, 603, 604, 610, 611, 612, 613, 614, 615, 624, 625, 627, 628, 633, 634, 635, 636, 637, 641, 642, 645, 648, 650, 651, 652, 653, 654, 655, 656, 657, 658, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 690, 691, 692, 693, 700, 701, 702, 703, 704, 705, 706, 707, 712, 713, 714, 715, 719, 720, 721, 722, 723, 724, 734, 735, 739, 740, 741, 744, 745, 747, 748, 749, 750, 753, 754, 757, 758, 761, 762, 763, 765, 766, 769, 770, 775, 778, 779, 801, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 833, 834, 837, 838, 839, 840, 841, 842, 843, 844, 846, 847, 848, 849, 854, 855, 856, 857, 858, 859, 860, 861, 863, 870, 871, 872, 873, 874, 875, 876, 878, 879, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 981, 982, 983, 984, 985, 986, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]
banned_abilities = [278]
randomize_abilities = 0
randomize_moves = 0
def check_banned_ability(index):
    if index in banned_abilities:
        return True
    return False

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

def randomizeAbilities(pokemon):
    if pokemon['is_present'] is True:
        if pokemon['species']['species'] == 934:
            choice = random.randint(1, 298)
            while check_banned_ability(choice) is True:
                choice = random.randint(1, 298)
            pokemon['ability_3'] = choice
        else:
            choice = random.randint(1, 298)
            i = 1
            while i < 4:
                if check_banned_ability(choice) is True:
                    choice = random.randint(1, 298)
                else:
                    pokemon["ability_" + str(i)] = choice
                    i = i + 1
            #pokemon['ability_1'] = random.randint(1, 298)
            #pokemon['ability_2'] = random.randint(1, 298)
            #pokemon['ability_3'] = random.randint(1, 298)
    return pokemon

def randomizeMoveset(pokemon):
    current_moveset = []
    if pokemon['is_present'] is True:
        for move in pokemon['levelup_moves']:
            index = random.randint(0, len(allowed_moves) - 1)
            if allowed_moves[index] not in current_moveset:
                move['move'] = allowed_moves[index]
                current_moveset.append(allowed_moves[index])

    return pokemon

def randomizeEvolutions(pokemon):
    for evo in pokemon['evo_data']:
        choice = random.randint(0, len(allowed_species) - 1)
        evo['species'] = allowed_species[choice]
        evo['form'] = get_alt_form(choice)
    return pokemon

def randomize(config):
    file = open(os.getcwd() + "/Randomizer/PersonalData/" +"personal_array_clean.json", "r")
    data = json.load(file)
    file.close()

    if config['ban_wonder_guard'] == "yes":
        banned_abilities.append(25)
    for pokemon in data['entry']:
        if config['randomize_abilities'] == "yes":
            pokemon = randomizeAbilities(pokemon)
        if config['randomize_movesets'] == "yes":
            pokemon = randomizeMoveset(pokemon)
        if config['randomize_evolutions'] == "yes":
            pokemon = randomizeEvolutions(pokemon)
    
    outdata = json.dumps(data, indent=4)
    with open(os.getcwd() + "/Randomizer/PersonalData/" +"personal_array.json", 'w') as outfile:
        outfile.write(outdata)
    print("Randomisation done !")

def main():
    randomize()

if __name__ == "__main__":
    main()
    