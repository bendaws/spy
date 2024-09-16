### Smallpy 1.0.0
### (C) Copyright 2024 Ben Daws.
### GNU GPL V3

import sys

version = "1.0.0"
copyright_details = "(C) Copyright 2024 Ben Daws"

args = sys.argv

if args[0] == "run":
    if args[1] != None:
        # write stuff here
        with open(args[1]) as file:
            for line in file.readlines():
                len_split = line.split(" ").lower()

                print(len_split) # Nothing to do heres

    else:
        print("Run flag given but no file given. (STOP)")
elif args[0] == "version":
    print("SmallPython {}. {}".format(version, copyright_details))