import json
import random
import os
allowed_moves = [1, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 97, 98, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 113, 114, 115, 116, 118, 120, 122, 123, 124, 126, 127, 129, 133, 135, 136, 137, 138, 139, 141, 143, 144, 147, 150, 151, 152, 153, 154, 156, 157, 161, 162, 163, 164, 165, 168, 172, 173, 174, 175, 178, 179, 180, 181, 182, 183, 184, 186, 187, 188, 189, 191, 192, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 217, 219, 220, 223, 224, 225, 226, 227, 229, 230, 231, 232, 234, 235, 236, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 259, 260, 261, 262, 263, 264, 266, 268, 269, 270, 271, 272, 273, 275, 276, 278, 280, 281, 282, 283, 284, 285, 286, 291, 292, 297, 298, 299, 303, 304, 305, 306, 307, 308, 309, 310, 311, 313, 314, 315, 317, 319, 321, 322, 323, 325, 326, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 347, 348, 349, 350, 351, 352, 355, 356, 359, 360, 361, 362, 364, 365, 366, 367, 368, 369, 370, 371, 372, 374, 379, 380, 383, 384, 385, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 427, 428, 430, 432, 433, 434, 435, 436, 437, 438, 440, 441, 442, 444, 446, 447, 449, 450, 451, 452, 453, 454, 455, 457, 458, 459, 460, 461, 463, 467, 468, 469, 470, 471, 472, 473, 474, 476, 478, 479, 482, 483, 484, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 499, 500, 501, 502, 503, 504, 505, 506, 508, 509, 510, 511, 512, 513, 514, 515, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 532, 533, 534, 535, 538, 539, 540, 541, 542, 547, 552, 555, 556, 557, 560, 562, 564, 565, 566, 568, 570, 572, 573, 574, 575, 577, 580, 581, 583, 584, 585, 586, 587, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 618, 619, 620, 621, 659, 660, 661, 662, 663, 665, 667, 668, 669, 670, 675, 676, 678, 679, 680, 681, 682, 683, 684, 686, 688, 689, 693, 694, 705, 706, 707, 709, 710, 715, 716, 744, 745, 746, 747, 748, 749, 750, 751, 752, 756, 776, 778, 780, 781, 782, 784, 785, 786, 787, 788, 789, 791, 793, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900]
# abilities are any number between 1 and 298, inclusive
banned_abilities = [278]
randomize_abilities = 0
randomize_moves = 0
def check_banned_ability(index):
    if index in banned_abilities:
        return True
    return False

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

def randomize(config):
    file = open(os.getcwd() + "/Randomizer/PersonalData/" +"personal_array_clean.json", "r")
    data = json.load(file)
    file.close()

    for pokemon in data['entry']:
        if config['randomize_abilities'] == "yes":
            pokemon = randomizeAbilities(pokemon)
        if config['randomize_movesets'] == "yes":
            pokemon = randomizeMoveset(pokemon)
    
    outdata = json.dumps(data, indent=4)
    with open(os.getcwd() + "/Randomizer/PersonalData/" +"personal_array.json", 'w') as outfile:
        outfile.write(outdata)
    print("Randomisation done !")

def main():
    randomize()

if __name__ == "__main__":
    main()
    