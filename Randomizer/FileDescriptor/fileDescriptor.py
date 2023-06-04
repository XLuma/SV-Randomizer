import json
import pathlib
import os
import fnvhash

def patchFileDescriptor():
    file = open(os.getcwd()+ "/Randomizer/FileDescriptor/data_clean.json")
    data = json.load(file)
    file.close()

    prefix = os.getcwd().replace("\\", '/') + "/output/romfs/"
    modPath = pathlib.Path(os.getcwd() + "/output/romfs")
    for item in modPath.rglob("*"):
        if item.is_file():
            name = item.__str__()
            name = name.replace("\\", "/")
            name = name.replace(prefix, "")
            #test= GFFNVHash(name)
            print(name.encode())
            hash = fnvhash.fnv1a_64(name.encode(), 0xCBF29CE484222645)
            print(hash)
            if hash in data['file_hashes']:
               index = data['file_hashes'].index(hash)
               data['file_hashes'].pop(index)
               data['files'].pop(index)

    outdata = json.dumps(data, indent=4)
    with open(os.getcwd() + "/Randomizer/FileDescriptor/" +"data.json", 'w') as outfile:
       outfile.write(outdata)
    outfile.close()
    print("Patched trpfd !")