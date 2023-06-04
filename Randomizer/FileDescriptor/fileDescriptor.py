import json
import pathlib
import os
import numpy
import fnvhash
import math

FNV_PRIME = numpy.uint64(0x00000100000001b3)
FNV_BASIS = numpy.uint64(0xCBF29CE484222645)

def GFFNVHash(path: str):
    buf = path.encode()
    result = FNV_BASIS
    for byte in buf:
        result = numpy.bitwise_xor(result, numpy.uint64(int(byte, 16)))
        #result ^= byte
        result *= FNV_PRIME
    return result

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