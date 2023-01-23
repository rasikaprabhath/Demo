import os


def working_directory():
    cwd = os.getcwd()
    return cwd

def make_directory():
    newdir1 = os.mkdir("D:\\Python\\pythonProject\\ScriptingWithPython\\testnewdir1")
    newdir2 = os.mkdir("D:\\testnewdir2")

def print_path(dir):
    path = os.path.abspath(dir)
    
    print(path)

cwd = working_directory()
print(cwd)

#make_directory()
print_path("GYB.txt")

