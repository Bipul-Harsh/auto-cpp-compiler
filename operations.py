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
        '''
        Gives editor name and file path

        Returns:
            (editor_name, editor_path)
        '''
        with open(self.editor_setting_file, 'r') as f:
            self.editor_name, self.editor_path = f.read().strip().split(' ')
            return (self.editor_name, self.editor_path)

class template(editor):
    def __init__(self):
        self.template_file = APP_PATH+'/template.cpp'
        editor.__init__(self)
    
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
    
    def check_file(self):
        '''
        Check file for filename error.
        '''
        return '.cpp' in self.file_path or '.CPP' in self.file_path

    def create_file(self, file, override):
        '''
        Create file in the present directory.
        '''
        self.file_path = self.pwd+'/'+file
        self.override = override
        assert self.check_file(),'File Extension Problem'
        if not os.path.exists(self.file_path) or override:
            os.system(f'cp {APP_PATH}/template.cpp {self.file_path}')
    
    def compile_file(self, output_file):
        '''
        Checks compiler and compiles the cpp file and generate ouput file in present directory.
        '''
        self.output_file = output_file
        assert os.popen(f'which {COMPILER}').read()[:-1],f'{COMPILER} is not installed in your system. Please install it and try again'
        os.system(f'{COMPILER} {self.file_path} -o {output_file}')
    
    def open_file(self):
        '''
        Opens the file in selected editor.
        '''
        os.system(f'{self.editor_path} {self.file_path}')
    
    def execute_output(self):
        '''
        Executes the output .out file.
        '''
        file_path = self.file_path.split('/')
        execute_command = '/'.join(file_path[:-1])+'/./'+self.output_file
        os.system(f'{execute_command}')