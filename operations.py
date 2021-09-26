import os

SYS_USER = os.popen('whoami').read()[:-1]
# APP_PATH = f'/home/{SYS_USER}/.acc' # actual path
APP_PATH = '/tmp/ramdisk/auto-cpp-compiler'
COMPILER = 'g++'

class editor:
    '''
    Text Editor Related Operations
    '''
    def __init__(self):
        # self.editor_file_path = f'/home/{self.user_name}/.acc/editor.txt'
        self.editor_setting_file = APP_PATH+'/editor.txt'
        try:
            self.get_editor()
        except ValueError:
            print("No editor info found, putting default editor.")
            try:
                self.set_editor('nano')
            except:
                print("Default editor nano isn't installed in your system. Please install it and try again :)")
                exit(1)
            self.get_editor()

    def find_editor(self, editor):
        '''
        Checks if editor exists and send its path using `which` command in linux

        Return:
            Returns path if program exists else return empty string

        Args:
            editor : editor name
        '''
        path = os.popen(f'which {editor}').read()[:-1]
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
                f.write(f'{editor_name} {path}')
            print(f"Changed Editor Info\n{editor_name} : {path}")
        except:
            print("You might have not installed the application. Please install and try again")
            exit(1)

    def get_editor(self):
        with open(self.editor_setting_file, 'r') as f:
            self.editor_name, self.editor_path = f.read().strip().split(' ')
            return (self.editor_name, self.editor_path)

class template(editor):
    def __init__(self):
        self.template_file = APP_PATH+'/template.cpp'
        editor.__init__(self)
    
    def get_template(self):
        with open(self.template_file, 'r') as f:
            file_content = f.read()
        return file_content
    
    def set_template(self):
        os.system(f'{self.editor_path} {APP_PATH}/template.cpp')
        print("Template Changed successfully")
        print('Updated Template\n\n'+self.get_template())

class file(editor):
    '''
    File Related Operations
    '''
    def __init__(self):
        self.pwd = os.popen('pwd').read()[:-1]
        editor.__init__(self)
        self.compiler = os.popen('which g++').read()[:-1]
        assert self.compiler,"g++ compiler doesnt exist in you system. Please first install it and then try again."
    
    def check_file(self):
        return '.cpp' in self.file_path or '.CPP' in self.file_path

    def create_file(self, file, override):
        self.file_path = self.pwd+'/'+file
        self.override = override
        assert self.check_file(),'File Extension Problem'
        if not os.path.exists(self.file_path) or override:
            os.system(f'cp {APP_PATH}/template.cpp {self.file_path}')
    
    def compile_file(self):
        assert os.popen(f'which {COMPILER}').read()[:-1],f'{COMPILER} is not installed in your system. Please install it and try again'
        output = os.popen(f'{COMPILER} {self.file_path}').read()[:-1]
        print('ff',output)