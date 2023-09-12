#!/usr/bin/python3
"""Module doc string"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    new_args = load_from_json_file('add_item.json')
except Exception:
    new_args = []

for arg in range(1, len(sys.argv)):
    new_args.append(sys.argv[arg])

save_to_json_file(new_args, 'add_item.json')
