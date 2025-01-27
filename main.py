import os

def run():
    dirlist = [f for f in os.listdir() if os.path.isdir(f)]
    for dirName in dirlist:
        print(f"{dirName}")
        os.chdir(dirName)
        filelist = [f for f in os.listdir() if os.path.isfile(f)]
        for filename in filelist:
            print(f"     {filename}")

        os.chdir('..')

def WalkDeepInFolder():
    f = []
    layer = 1
    w = os.walk(".venv")
    for (dirpath, dirnames, filenames) in w:
        #print(f"{dirpath}    {dirnames}    {filenames}")
        if layer == 1:
            print(f"{dirpath}    {dirnames}    {filenames}")
            f.extend(dirnames)
            break
        layer += 1

def ChangeDirectory():
    os.chdir(".venv")
    dirlist = [f for f in os.listdir() if os.path.isdir(f)]
    for dirName in dirlist:
        print(dirName)

if(__name__ == '__main__'):
    run()