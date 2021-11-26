#!/usr/bin/python3
import argparse
import os
import platform

import operations
# Initialising operation module
try:
    file_opr = operations.file()
    editor_opr = operations.editor()
    template_opr = operations.template()
    system_settings = operations.system_settings()
except FileNotFoundError:
    print("File is not found. Please install the program first.")

VERSION = "1.0.0"

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
    description=LOGO,
    epilog='''\
Example:
    > acc prog.cpp
    > acc --ct
    > acc --ce vim
    > acc prog.cpp -eo output.out
        
For any issue visit:\nhttps://github.com/Bipul-Harsh/auto-cpp-compiler/issues''')

parser.add_argument('file', type=str, default='', help="to create/open file.",nargs='?')
parser.add_argument('-o', action='store_const', const=True, default=False, dest='override_file', help="Override if file exists with template file.")
parser.add_argument('--ct', action='store_const', const=True, default=False, dest='update_template', help="Change file template.")
parser.add_argument('--st', action='store_const', const=True, default=False, dest='show_template', help="Show file template.")
parser.add_argument('--ce', type=str, help="Change text editor of your choice (vim and gedit is preffered).")
parser.add_argument('--se', action='store_const', const=True, default=False, dest='show_editor', help="Show selected text editor.")
parser.add_argument('--version', action='store_const', const=True, default=False, dest='version', help="Show current version.")
parser.add_argument('-eo', type=str, help="For storing the ouput file explicitly. Please output file name after it!")
parser.add_argument('--uninstall', action='store_const', const=True, default=False, dest='uninstall', help="To uninstall %(prog)s program :(")

args = parser.parse_args()

FILE = args.file
OVERRIDE_FILE = args.override_file
CHANGE_EDITOR = bool(args.ce) #Empty string makes false
EDITOR = args.ce
CHANGE_TEMPLATE = args.update_template
SHOW_VERSION = args.version
SHOW_EDITOR = args.show_editor
SHOW_TEMPLATE = args.show_template
OUTPUT_FILE = args.eo
DO_UNINSTALL = args.uninstall

print(OUTPUT_FILE)

# Check if the user didnt put anything
is_settings_related = bool(CHANGE_EDITOR or DO_UNINSTALL or CHANGE_TEMPLATE or SHOW_VERSION or SHOW_TEMPLATE or SHOW_EDITOR)
assert bool(FILE or is_settings_related),"Please provide a file name"
assert ('-eo' not in FILE), "Please provide an output file name"

# All Query Task
if is_settings_related:
    print(LOGO+'Does repetitve compiling task of .cpp file for you :)\n'+"--------------------------------------------------------------------------------------")
    if SHOW_VERSION:
        print(f'\nVersion : {VERSION}')
    if SHOW_EDITOR:
        editor_name, editor_location = editor_opr.get_editor()
        print("\nCurrently Selected Editor\n"+editor_name+' : '+editor_location)
    if CHANGE_EDITOR:
        editor_opr.set_editor(EDITOR)
    if SHOW_TEMPLATE:
        print('\nTemplate\n------------------------------------------------------------------------------------\n'
            + template_opr.get_template()
            + '\n------------------------------------------------------------------------------------')
    if CHANGE_TEMPLATE:
        template_opr.set_template()
    if DO_UNINSTALL:
        confirm = ''
        while(confirm not in ['y','n']):
            confirm = input("Are you sure to uninstall this software (y/n): ").strip().lower()
            if confirm=='y':
                system_settings.uninstall()
            elif confirm=='n':
                exit(0)
    exit(0)

# File Operations
file_opr.create_file(FILE, OVERRIDE_FILE)
in_loop = True
opr = 'd'
while in_loop:
    # if platform.system() == 'Windows':
    #     os.system('cls')
    # else:
    #     os.system('clear')
    if opr=='o' or opr=='d':
        print('opr: ', opr)
        file_opr.open_file()
        file_opr.compile_file(OUTPUT_FILE)
    print('Ouput\n------------------------------------------------------------------------------------')
    file_opr.execute_output()
    print('------------------------------------------------------------------------------------')
    opr=''
    while opr not in ['e','o','r']:
        opr = input('Enter [o open] [e exit] [r rerun]: ').lower()
        # Deleting the output file
        file_opr.delete_output()
        if opr == 'e':
            exit(0)
        elif opr not in ['o','r']:
            print('Invalid Input')