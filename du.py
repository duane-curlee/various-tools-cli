import os
from argparse import ArgumentParser
from glob import glob
"""
This utility is some-what like the Unix/Linux du command, with some
limits. I plan to build on this script, check back for updates.
"""

def parse_input():
    parser = ArgumentParser(description = 'Shows file and folder disk usage')
    parser.add_argument('items', nargs = '*',
                help = 'File or Folder name(s) to size up, wildcards welcome')
    parser.add_argument('-c', '--csv', action = "store_true",
                help = 'Changes the default output to comma separated values (CSV)')
    parser.add_argument('-v', '--verbose', action = "store_true",
                help='Enable verbose mode')
    
    return parser.parse_args()

def size_up_dir(the_dir):
    total_size = 0
    for root, dirs, files in os.walk(the_dir):
        for our_file in files:
            total_size += os.path.getsize(os.path.join(root, our_file))
        for our_dir in dirs:
            total_size += 4096

    return total_size

def size_up_files(the_files):
    total_size = 0
    for our_file in the_files:
        total_size += os.path.getsize(our_file)

    return total_size

def human_readable(num_bytes):
    a_gig = 1073741824
    a_meg = 1048576
    a_kil = 1024
    ideal_str_size = 10

    if num_bytes >= a_gig:
        str_sizer = '{:.2f} GB'.format(num_bytes / a_gig)
    elif num_bytes >= a_meg:
        str_sizer = '{:.2f} MB'.format(num_bytes / a_meg)
    elif num_bytes >= a_kil:
        str_sizer = '{:.2f} KB'.format(num_bytes / a_kil)
    elif num_bytes == 1:
        str_sizer = '1 byte'
    elif num_bytes == 0:
        str_sizer = 'zero bytes'
    elif num_bytes < 0:
        str_sizer = 'negative number'
    else:
        str_sizer = '%d bytes' % num_bytes

    return str_sizer.rjust(ideal_str_size, ' ')

if __name__ == '__main__':
    grand_total_size = 0
    item_list = list()
    args = parse_input()

    if args.items:
        for current_arg in args.items:
            for current_item in glob(current_arg):
                item_list.append(current_item)
    else:
        item_list.append(os.getcwd())

    for our_item in item_list:
        if os.path.isdir(our_item):
            this_size = size_up_dir(our_item)
            grand_total_size += this_size
            if args.csv:
                print('%s,"%s"' % (this_size, our_item))
            else:
                print('Size: %s folder: %s' % (human_readable(this_size), our_item))
        elif os.path.isfile(our_item):
            this_size = os.path.getsize(our_item)
            grand_total_size += this_size
            if args.csv:
                print('%s,"%s"' % (this_size, our_item))
            else:
                print('Size: %s   file: %s' % (human_readable(this_size), our_item))
        else:
            if args.verbose:
                print('Skipping, what is this? :', our_item)

    print('   Grand total size:', human_readable(grand_total_size))

