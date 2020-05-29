#!/usr/bin/python
import os
from time import ctime
from glob import glob
from argparse import ArgumentParser
"""
This utility displays the three date and
time stamps on files and folders.
"""

def parse_input():
    parser = ArgumentParser(description =
        "This utility displays the three date and\
        time stamps on files and folders")
    parser.add_argument('items', nargs = '*',
                help = 'Filename(s) to see the date and time stamps')
    
    return parser.parse_args()

def show_times(the_file):
    print('     === Item :', the_file, ' ===')
    print('      Created : ', (ctime(os.path.getctime(the_file))))
    print('Last modified : ', (ctime(os.path.getmtime(the_file))))
    print('Last accessed : ', (ctime(os.path.getatime(the_file))))

if __name__ == '__main__':
    args = parse_input()
    item_list = list()

    if args.items:
        for current_arg in args.items:
            for current_item in glob(current_arg):
                item_list.append(current_item)
    else:
        for current_item in os.listdir():
            item_list.append(current_item)

    for current_file in item_list:
        show_times(current_file)
