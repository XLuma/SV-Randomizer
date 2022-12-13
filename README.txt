--- Pokemon Scarlet and Violet Randomizer by XLuma ----

*** THIS RANDOMIZER WORKS ONLY WITH VERSION 1.0.1 AND ABOVE, DO NOT USE 1.0 AS YOUR GAME UPDATE ***
PREFACE: Make sure you have at least Python 3.10 installed on your computer, anything lower will not work!
PS: If after installing, and running the randomize batch script you see the Microsoft store open instead, in your windows search bar type "Manage App Execution Aliases" and turn off the ones that have "python.exe" and "python3.exe" under them (They are named App Installer)

HOW TO USE:

- If not done, install Python 3.10 from either the Microsoft Store, or the official python website

Step 1: Open the config.json in any text editor (even notepad works) and configure the file how you want it. To enable an option, type yes between quotes. If you want to disable , then type no instead.
Step 2: Save your edits to the config.json, and double click the randomize.bat file. A window will appear with some logs, and eventually a Press Enter to continue will appear, then you can close that window.
Step 3: A new folder called "output" will be created. Go inside of it, and you will see a romfs folder as well as a randomizer.zip file. The randomizer.zip is the compressed, ready-to-use modpack to be imported in Trinity Mod Loader. a romfs folder is still provided if you want to use an alternative patching method.
Step 4: Open Trinity Loader, click "Add Mod" and select the randomizer.zip inside the output folder, make sure it is ticked in the window, and then click Apply mod. Copy the resulting romfs folder to your mods folder on your switch or emulator, and launch the game
Step 5: Enjoy :)

TITLEID'S

Scarlet: 0100A3D008C5C000
Violet: 01008F6008C5E000

--- General Info ----

This is a rework of my previous randomizer that I made via code injection. This randomizer went through multiple reworks, at first having individual randomizers, now to having an easy-to-use configuration file
and program that does all the randomization and packaging for you. It currently randomizes Wild Encounters, Trainers, Static encounters, Personal Data (Abilities, and Movesets), Starters (and all gifted pokemons by extension),
and also provides a few extra options to customize your randomisation. It packages the resulting randomization to a zip file in the output folder, so all you need to do is import it in Trinity Loader and apply the mod.

If you use this program for content, credits in the description is not required, but always appreciated ! If there are any problems with the program whatsoever, yall know where to find me :)

KNOWM BUGS/ISSUES

- Palafin and his alt form will not get their normal ability randomized, due to being absolute garbage without it (and then game crashing if the ability is given via PkHex). Thus, only the hidden ability is randomized. Furthermore, no other pokemon can obtain the Zero to Hero ability.
- Following the first issue: Some abilities might not work in game, like form-changing abilities. If such a case ever happens, please let me know.
