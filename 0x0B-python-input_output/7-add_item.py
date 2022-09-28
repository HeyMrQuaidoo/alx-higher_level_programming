#!/usr/bin/python3
"""Module for file input/output"""

import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
write_file = __import__('1-write_file').write_file

name_file = "add_item.json"

if not os.path.exists(name_file):
    write_file(name_file, "[]")

new_list = load_from_json_file(name_file)
argc = len(sys.argv)
for i in range(1, argc):
    new_list += [sys.argv[i]]

save_to_json_file(new_list, name_file)
