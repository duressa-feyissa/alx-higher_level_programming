#!/usr/bin/python3
from sys import argv
from os.path import exists
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


argc = len(argv)
if True:
    new = []
    if exists("add_item.json"):
        hold = load_from_json_file("add_item.json")
        for i in range(argc):
            if i != 0:
                hold.append(argv[i])
        save_to_json_file(hold, "add_item.json")
    else:
        save_to_json_file(new, "add_item.json")
