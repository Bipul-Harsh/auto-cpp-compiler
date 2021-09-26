#!/usr/bin/python3

import os
import argparse
import operations

file_opr = operations.file()
editor_opr = operations.editor()
template_opr = operations.template()

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
parser.add_argument('-o', action='store_const', const=True, default=False, dest='override_file', help="Override if file exists with template file.")
parser.add_argument('file', type=str, default='', help="to create/open file.",nargs='?')
parser.add_argument('--ct', action='store_const', const=True, default=False, dest='update_template', help="Change file template.")
parser.add_argument('--st', action='store_const', const=True, default=False, dest='show_template', help="Show file template.")
parser.add_argument('--ce', type=str, help="Change text editor of your choice (vim and gedit is preffered).")
parser.add_argument('--se', action='store_const', const=True, default=False, dest='show_editor', help="Show selected text editor.")
parser.add_argument('--version', action='store_const', const=True, default=False, dest='version', help="Show current version.")
parser.add_argument('--uninstall', action='store_const', const=True, default=False, dest='uninstall', help="To uninstall %(prog)s program :(")

args = parser.parse_args()

FILE = args.file.replace(' ', '_')
OVERRIDE_FILE = args.override_file
CHANGE_EDITOR = bool(args.ce) #Empty string makes false
EDITOR = args.ce
CHANGE_TEMPLATE = args.update_template
SHOW_VERSION = args.version
DO_UNINSTALL = args.uninstall
SHOW_EDITOR = args.show_editor
SHOW_TEMPLATE = args.show_template

# Check if the user didnt put anything
is_settings_related = bool(CHANGE_EDITOR or DO_UNINSTALL or CHANGE_TEMPLATE or SHOW_VERSION or SHOW_TEMPLATE or SHOW_EDITOR)
assert bool(FILE or is_settings_related),"Please provide a file name"

# All Query Task

if is_settings_related:
    print(LOGO+"--------------------------------------------------------------------------------------")
    if SHOW_VERSION:
        print('Version : 1.0.0')
    if SHOW_EDITOR:
        editor_name, editor_location = editor_opr.get_editor()
        print("Currently Selected Editor\n"+editor_name+' : '+editor_location)
    if CHANGE_EDITOR:
        editor_opr.set_editor(EDITOR)
    if SHOW_TEMPLATE:
        print('Template\n\n'+template_opr.get_template())
    if CHANGE_TEMPLATE:
        template_opr.set_template()
    
    exit(0)

# File Operations
file_opr.create_file(FILE, OVERRIDE_FILE)