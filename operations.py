import os
import shutil
import sys
import platform

SYS_USER = os.getlogin()
COMPILER = 'g++'
ISSUES_LINK = 'https://github.com/Bipul-Harsh/auto-cpp-compiler/issues'
PLATFORM = platform.system()

class system_settings:
    def __init__(self, installation_dir=''):
        self.get_path_progressor()
        curr_dir = os.getcwd()
        argument = f'{self.pp}'.join(sys.argv[0].strip().split(f'{self.pp}')[:-1])
        argument = argument.rstrip(f'{self.pp}.')
        if not argument:
            # Ex: ./main.py
            self.APP_PATH = curr_dir
        elif argument and argument[0]=='.':
            # Ex: ./auto-cpp-compiler/./main.py
            self.APP_PATH = curr_dir + self.pp + argument.lstrip()
        else:
            # Ex: /home/user/..../auto-cpp-compiler/main.py | C:\\Users\\...\\auto-cpp-compiler\\main.py
            self.APP_PATH = argument
        
        assert self.all_files_exists(self.APP_PATH),"Required files arent present in the directory.\nPlease reinstall the application!"
    
    def all_files_exists(self, path):
        required_file_path = path + self.pp+'.required'
        assert os.path.exists(required_file_path),".required file is not present in the directory."
        with open(required_file_path, 'r') as f:
            files = f.read().split('\n')
        for file in files:
            if not os.path.exists(f'{path}{self.pp}{file}'):
                return False
        else:
            return True

    def get_path_progressor(self):
        '''Windows has unfortunately different way to progress through directories
        \n`pp` stands for path progressor
        '''
        if PLATFORM == "Windows":
            self.pp = '\\'
        else:
            self.pp = '/'

    def uninstall(self):
        assert os.path.isdir(self.APP_PATH),"Resource cannot be found.\nYou might haven't installed this software yet."
        shutil.rmtree(self.APP_PATH)
        if PLATFORM == "Linux":
            symlink_path = "/usr/local/bin/acc"
            if os.path.exists(symlink_path):
                os.system(f"sudo rm {symlink_path}")
        
        print(f"\nProgram uninstalled successfully.\n\nPlease let me know for any issues you have faced at:\n{ISSUES_LINK}")

class editor(system_settings):
    '''
    Text Editor Related Operations
    '''
    def __init__(self, installation_dir=''):
        system_settings.__init__(self, installation_dir)
        self.editor_setting_file = self.APP_PATH+f'{self.pp}.editor'
        self.file_check()
        try:
            self.get_editor()
        except ValueError:
            #No editor info found, putting default editor.
            editors = ['nano','vim','neovim','emacs','gedit','notepad']
            got_any = False
            for editor in editors:
                try:
                    self.set_editor(editor)
                    self.get_editor()
                    got_any = True
                    break
                except:
                    pass
            if not got_any:
                print(f"You system doesnt have any of these text editors:\n"+'\n'.join(editors)+'\nPlease install any of them to get started.')
                sys.exit(0)

    def file_check(self):
        '''
        Checks if editor file exists, if not creates it.
        '''
        if not os.path.exists(self.editor_setting_file):
            with open(self.editor_setting_file, 'w') as f:
                pass

    def find_editor(self, editor):
        '''
        Checks if editor exists and send its path using `which` command in linux

        Return:
            Returns path if program exists else return empty string

        Args:
            editor : editor name
        '''
        path = shutil.which(editor)
        assert path,f"{editor} editor doesnt exist in you system. Please first install it and then try again."
        return path

    def set_editor(self, editor_name):
        '''
        Change the editor

        Args:
            editor_name : name through which you open file in editor through shell
            Example:
                vim <file>
                gedit <file>
                nano <file>
            
        Dependency:
            editor.find_editor() : to check if editor exists  
        '''
        path = self.find_editor(editor_name)
        try:
            with open(self.editor_setting_file, 'w') as f:
                f.write(f'{editor_name}|{path}')
            print(f"Changed Editor Info\n{editor_name} : {path}")
        except:
            print("You might have not installed the application. Please install and try again")
            sys.exit(1)

    def get_editor(self):
        '''
        Gives editor name and file path

        Returns:
            (editor_name, editor_path)
        '''
        with open(self.editor_setting_file, 'r') as f:
            self.editor_name, self.editor_path = f.read().strip().split('|')
        return (self.editor_name, self.editor_path)

class template(editor):
    def __init__(self, installation_dir = ''):
        editor.__init__(self, installation_dir)
        self.template_file = self.APP_PATH+'/template.cpp'
    
    def get_template(self):
        '''
        Return template.cpp file content as a string.
        '''
        with open(self.template_file, 'r') as f:
            file_content = f.read()
        return file_content
    
    def set_template(self):
        '''
        Opens the template.cpp file in editor to make some changes in it.
        '''
        os.system(f'{self.editor_path} {self.APP_PATH}{self.pp}template.cpp')
        print("Template Changed successfully")
        print('Updated Template\n\n'+self.get_template())

class file(template):
    '''
    File Related Operations
    '''
    def __init__(self):
        self.pwd = os.getcwd()
        template.__init__(self)
    
    def check_file(self):
        '''
        Check file for filename error.
        '''
        return '.cpp' in self.file_path or '.CPP' in self.file_path

    def create_file(self, file, override):
        '''
        Create file in the present directory.
        '''
        self.file_path = '\"'+self.pwd+f'{self.pp}'+file+'\"'
        self.override = override
        assert self.check_file(),'File Extension Problem'
        if not os.path.exists(self.file_path.strip('\"')) or override:
            with open(self.file_path.strip('\"'), 'w') as f:
                f.write(self.get_template())
    
    def compile_file(self, output_file):
        '''
        Checks compiler and compiles the cpp file and generate ouput file in present directory.
        '''
        if output_file:
            self.output_file = '\"'+output_file+'\"'
            self.explicit_output = True
        else:
            self.output_file = "a.out"
            self.explicit_output = False
        assert shutil.which(COMPILER),f'{COMPILER} is not installed in your system. Please install it and try again'
        os.system(f'{COMPILER} {self.file_path} -o {self.output_file}')
    
    def open_file(self):
        '''
        Opens the file in selected editor.
        '''
        os.system(f'{self.editor_name} {self.file_path}')
    
    def execute_output(self):
        '''
        Executes the output .out file.
        '''
        file_path = self.file_path.split(f'{self.pp}')
        self.execute_command = f'{self.pp}'.join(file_path[:-1])+f'{self.pp}.{self.pp}'+self.output_file
        self.execute_command = self.execute_command[1:]
        os.system(f'{self.execute_command}')
    
    def delete_output(self):
        '''
        Removes the output file.
        '''
        if not self.explicit_output and os.path.exists(self.execute_command):
            os.remove(self.output_file.strip('\"'))