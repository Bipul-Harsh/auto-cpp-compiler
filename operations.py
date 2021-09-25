import os

class file:
    '''
    File Related Operations
    '''
    def __init__(self):
        self.file_path = ''
        self.user_name = os.popen('whoami').read()[:-1]
        # self.app_path = f'/home/{self.user_name}/.acc/' #The actual path
        self.app_path = f'/tmp/ramdisk/auto-cpp-compiler'

    def create_file(self, file):
        self.file_path = file
        print(self.file_path, os.path.exists(self.file_path))
        if os.path.exists(self.file_path):
            print("File already exists\n\nOPTIONS\n1 : Replace with new\n2 : Use the existing file without any update\n")
            action = int(input('Enter your choice: ').strip())
            if action == 1:
                os.system(f'cp {self.app_path}/template.cpp {self.file_path}')
            elif action != 2:
                print("Wrong choice\n")
                exit(-1)
        else:
            os.system(f'cp {self.app_path}/template.cpp {self.file_path}')