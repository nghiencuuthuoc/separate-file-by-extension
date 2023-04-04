from os import *
import shutil

def makeDir(DirectoryName):
    if path.exists(DirectoryName)==False: mkdir(DirectoryName)

def movefile(item):
    extName=path.splitext(item.name)[1][1:]
    try:
        if extName != '':
            makeDir(extName)
            shutil.move(item, extName)
        elif extName == '' and item.name[0][0]!='.':
            makeDir('NoExt')
            shutil.move(item, 'NoExt')
        else:
            makeDir('NoName')
            shutil.move(item, 'NoName')
    except:
        None

chdir(path.dirname(__file__))

for file in scandir(getcwd()):
    movefile(file) if path.isfile(file) and file.name != path.basename(__file__) else None