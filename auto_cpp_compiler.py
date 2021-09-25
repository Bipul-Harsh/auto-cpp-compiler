#!/usr/bin/python3

import os
import argparse
import operations

LOGO = '''\
    _         _           ____ ____  ____     ____                      _ _           
   / \  _   _| |_ ___    / ___|  _ \|  _ \   / ___|___  _ __ ___  _ __ (_) | ___ _ __ 
  / _ \| | | | __/ _ \  | |   | |_) | |_) | | |   / _ \| '_ ` _ \| '_ \| | |/ _ \ '__|
 / ___ \ |_| | || (_) | | |___|  __/|  __/  | |__| (_) | | | | | | |_) | | |  __/ |   
/_/   \_\__,_|\__\___/   \____|_|   |_|      \____\___/|_| |_| |_| .__/|_|_|\___|_|   
                                                                 |_|                      
'''

parser = argparse.ArgumentParser(
    prog="Auto CPP Compiler",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    usage="Does repetitve compiling task of .cpp file for you :)",
    description=LOGO,
    epilog='''\
Example:
    > acc prog.cpp
    > acc --ct
    > acc --ce vim
        
For any issue contact me at bipulharsh123@gmail.com''')
parser.add_argument('file', type=str, default='', help="to create/open file.",nargs='?')
parser.add_argument('--ct', action='store_const', const=True, default=False, dest='update_template', help="Change file template.")
parser.add_argument('--st', action='store_const', const=True, default=False, dest='show_template', help="Show file template.")
parser.add_argument('--ce', type=str, help="Change text editor of your choice (vim and gedit is preffered).")
parser.add_argument('--se', action='store_const', const=True, default=False, dest='show_editor', help="Show selected text editor.")
parser.add_argument('--version', action='store_const', const=True, default=False, dest='version', help="Show current version.")
parser.add_argument('--uninstall', action='store_const', const=True, default=False, dest='uninstall', help="To uninstall %(prog)s program :(")

args = parser.parse_args()

FILE = args.file.replace(' ', '_')
UPDATE_EDITOR = args.ce
UPDATE_TEMPLATE = args.update_template
SHOW_VERSION = args.version
DO_UNINSTALL = args.uninstall
SHOW_EDITOR = args.show_editor
SHOW_TEMPLATE = args.show_template

# Check if the user didnt put anything
assert bool(FILE or UPDATE_EDITOR or DO_UNINSTALL or UPDATE_TEMPLATE or SHOW_VERSION or SHOW_TEMPLATE or SHOW_EDITOR),"Please provide a file name"

if SHOW_VERSION:
    print(LOGO+'Version : 1.0.0')
    exit(0)

# File extension check
assert '.cpp' in FILE or '.CPP' in FILE,'File Extension Problem'

PWD = os.popen('pwd').read()[:-1]
FILE = PWD+'/'+FILE
print(FILE)

file_opr = operations.file()
file_opr.create_file(FILE)

print(os.path.exists(FILE))