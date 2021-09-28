#!/usr/bin/python3

import platform
import os
import getpass
import sys

import operations

curr_dir = os.getcwd().split('/')
argument = sys.argv[0].split('/')[:-1]
if len(argument) > 0 and argument[-1] == '.':
    argument = argument[:-1]
INSTALLATION_DIR = '/'.join(curr_dir+argument)
print(INSTALLATION_DIR)

editor_opr = operations.editor(INSTALLATION_DIR)
template_opr = operations.template(INSTALLATION_DIR)

USER = getpass.getuser()

APP_DIR_NAME = '.acc'
# LINUX_APP_PATH = f'/home/{USER}'
LINUX_APP_PATH = '/tmp/ramdisk/'
WINDOWS_APP_PATH = ''
MAC_APP_PATH = ''

PLATFORM = platform.system()

class installing_process():
    def __init__(self):
        self.get_app_path()
    
    def get_app_path(self):
        if PLATFORM == 'Linux':
            self.app_path = f'{LINUX_APP_PATH}/{APP_DIR_NAME}'
        elif PLATFORM == 'Mac':
            self.app_path = f'{MAC_APP_PATH}/{APP_DIR_NAME}'
        elif PLATFORM == 'Windows':
            self.app_path = f'{WINDOWS_APP_PATH}/{APP_DIR_NAME}'
        else:
            print('This software doesnt support this system yet :(\nPlease let us know your system to extend our application compatibility with it.')
            exit(1)

    def create_app_dir(self):
        assert not os.path.isdir(self.app_path),"Program already installed."
        os.mkdir(self.app_path)
    
    def put_template_file(self):
        opr = ''
        while(opr.lower() != 'c'):
            print("Default Template\n--------------------------------")
            # print(template_opr.get_template())
            opr = input('\n--------------------------------\nSave above default Template [u to_update] [c confirmed] : ').strip().lower()
    
    def do_installation(self):
        print(f"System : {PLATFORM} {platform.release()}")
        # self.create_app_dir()

if __name__ == '__main__':
    installation = installing_process()
    installation.do_installation()