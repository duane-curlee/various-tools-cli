import os
from argparse import ArgumentParser
"""
This utility checks to see if a file exists, and is also case sensitive.
This is very handy on a Microsoft Windows platform, which is not a
case-sensitive operating system. This is unneeded on Linux and Apple
computers.

This script file\_exist\_case.py only exists to preserve the function
file\_exists\_case() which can be copied to your own Python script if
you need this funtionality. This function accepts a filename only, not a
folder name, it then does a case-sensetive exisitance check, and returns
True or False.
"""
def parse_cmd_line():
    parser = ArgumentParser(description = 'Case-sensitive file existance checker',
        prog = 'file_exists_case.py',
        epilog = "This Python command-line script will check all arguments you\
        provide and check and see if those files exists. This check is\
        case-sensitive which is handy for Windows users, but unnessessary for\
        Linux, Unix and Mac users.")
    parser.add_argument('filenames', nargs='+', metavar = 'filename',
        help = 'Filename(s) to existance check')

    return parser.parse_args()

def file_exists_case(the_file):
    if not os.path.isfile(the_file):
        return False

    directory, filename = os.path.split(the_file)

    if directory == '':
        directory = os.getcwd()

    return filename in os.listdir(directory)

if __name__ == '__main__':
    args = parse_cmd_line()

    for the_arg in args.filenames:
        if file_exists_case(the_arg):
            print('          Exists :', the_arg)
        else:
            print('  Does not exist :', the_arg)
