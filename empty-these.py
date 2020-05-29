from argparse import ArgumentParser
import os
from shutil import rmtree
from glob import glob
"""
This utility will remove all files and folders from your specified
folder, but it will not remove the folder itself.
It will not prompt if you are sure, be sure before you execute.
It will only empty whole directories, not individual files.
Wildcards are accepted, be careful with them.
"""

def parse_input():
    parser = ArgumentParser(description = 'Folder empty\'er',
        epilog = "This Python command-line script will delete all\
        files and folders within the folder(s) you provide on the\
        command line. You get no warnings. Sit on your hands\
        before pressing Enter.")
    parser.add_argument('-v', '--verbose', action = 'store_true',
        help = 'Enable verbose mode')
    parser.add_argument('folders', nargs='+',
        help = 'Folder name(s) (required) to empty')

    return parser.parse_args()

def empty_this_nt(the_folder):
    if args.verbose: print('Running attrib command ...', end=' ')
    attrib_cmd = 'attrib -h -s -r /S /D /L \"' + the_folder + '\\*.*\"'
    os.system(attrib_cmd)
    if args.verbose: print('Done.')

    for current_item in os.listdir(the_folder):
        current_item = os.path.join(the_folder, current_item)

        if os.path.isdir(current_item):
            if args.verbose: print('Deleting directory :', current_item)
            rmtree(current_item)
        elif os.path.isfile(current_item):
            if args.verbose: print('Deleting file      :', current_item)
            os.remove(current_item)
        else:
            print('What is this? :', current_item)

if __name__ == '__main__':
    args = parse_input()

    for current_arg in args.folders:
        for current_dir in glob(current_arg):
            current_dir = os.path.abspath(current_dir)

            if os.path.isdir(current_dir):
                print('Emptying:', current_dir)
                empty_this_nt(current_dir)
            elif os.path.exists(current_dir):
                print('Skipping, not a directory:', current_dir)
            else:
                print('Directory not found:', current_dir)

