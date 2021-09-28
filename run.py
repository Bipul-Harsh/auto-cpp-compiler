#!/usr/bin/python3

import sys
import os
import platform

PLATFORM = platform.system()

FILE = sys.argv[1]

if PLATFORM == 'Windows':
    pass

elif PLATFORM == "LINUX":
    # APP_PATH = '/home/bhworld/.local/bin/acc'
    APP_PATH = '/tmp/ramdisk/auto-cpp-compiler'
    os.system(f'{APP_PATH}/./main.py {FILE}')