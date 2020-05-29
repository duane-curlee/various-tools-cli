#!/usr/bin/python
import os
import zipfile
from argparse import ArgumentParser
from glob import glob
from datetime import datetime

def parse_input():
    parser = ArgumentParser(description = 'Archive Them',
        prog = 'arcem.py',
        epilog = "This Python command-line script will place your\
        files and/or folders into a zip file with a date-time-stamp.")
    parser.add_argument('-v', '--verbose',   action="store_true",
        help='Enable verbose mode')
    parser.add_argument('items', nargs='+', metavar = 'items',
        help = 'File and/or Folder names (required) for archiving, wildcards welcome')

    return parser.parse_args()

if __name__ == '__main__':
    something_found = False
    skip_dot_dirs = True
    skip_empty_dirs = True
    skip_backup_files = True

    our_cwd = os.getcwd()
    args = parse_input()

    my_now = datetime.now()
    my_fname = 'backup-' + my_now.strftime('%Y-%m-%d-%H-%M-%S') + '.zip'
    my_zip = zipfile.ZipFile(my_fname, 'w')

    for the_item in args.items:
        for this_item in glob(the_item):
            if os.path.isdir(this_item):
                for root, dirs, files in os.walk(this_item):
                    if skip_dot_dirs is True:
                        dirs[:] = [d for d in dirs if not d.startswith('.')]
                    if skip_backup_files is True:
                        files[:] = [f for f in files if not f.startswith('backup-')]
                    for name in files:
                        arc_name = os.path.join(root, name)
                        if args.verbose:
                            print('Archiving: ' + arc_name)
                        my_zip.write(arc_name, compress_type=zipfile.ZIP_DEFLATED)
                        something_found = True
                    if skip_empty_dirs is False:
                        for name in dirs:
                            my_zip.write(os.path.join(root, name),
                                         compress_type=zipfile.ZIP_DEFLATED)
            elif os.path.isfile(this_item):
                if args.verbose:
                    print('Archiving: ' + this_item)
                my_zip.write(this_item, compress_type=zipfile.ZIP_DEFLATED)
                something_found = True
            else:
                if args.verbose:
                    print('Skipping, file or folder not found: ' + this_item)

    my_zip.close()

    if something_found == True:
        print('Folders archived into:', my_fname)
    else:
        os.remove(my_zip.filename)
        print('No files or folders found, no archive created.')

