#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Usage:
  removeBakFile.py [-s] [-e]
  removeBakFile.py dir <dir> [<exts>] [-s] [-e]
  removeBakFile.py <exts> [-s] [-e]


Options:
  -h --help     Show this screen
  -s            silent remove
  -e            remove empty folder
  dir           dir, if none use current dir
  exts          bakfile ext. if none default 'bak'. more ext:'bak,bak2,...'
"""

import os
import os.path
from docopt import docopt

def getFileList(dir):
    fileList = []
    dirList = []
    for root, dirs, files in os.walk(dir):
        
        for dir in dirs:
            dir = root + '/' + dir
            dir = dir.replace('\\','/')
            dirList.append(dir)

        for name in files:
            filePath = root + '/' + name
            filePath = filePath.replace('\\','/')
            fileList.append(filePath)

    return fileList, dirList

def grepList(fileList,exts=['bak']):
    targetList =[]

    for filePath in fileList:
        ext = filePath.split('.')[-1]
        if ext in exts:
            targetList.append(filePath)

    return targetList

def removeBakFiles(dir, exts=[], silent=False, empty=False):
    fileList = []
    dirs = []
    fileList, dirs = getFileList(dir)

    if len(exts):
        exts = exts.split(',')
        targetList = grepList(fileList,exts)
    else:
        targetList = grepList(fileList)
    
    if not silent:        
        print('==== Remove List ====')
        for filePath in targetList:
            print(filePath)
        print("You confirm remove file in this list[y/n]: ")
        confirm = input()
        confirm = confirm.lower()
        if confirm == 'y':
            for filePath in targetList:
                os.remove(filePath)     
            print('Remove list finish.')        
        else:
            print('Cancel remove list.')
    else:
        for filePath in targetList:
            os.remove(filePath)

    if not silent:     
        print('==== Remove Empty Folder List ====')

    if empty:        
        while True:
            dirs,removeList = removeEmptyFolder(dirs)
            if (not silent) and removeList:
                for l in removeList:
                    print('Remove empty folder: %s' % l)
            if not removeList: break

def removeEmptyFolder(dirs):
    removeList = []
    
    for dir in dirs:
        if not os.listdir(dir):
            os.rmdir(dir)
            removeList.append(dir)
            dirs.remove(dir)   

    return dirs,removeList

def main():
    args = docopt(__doc__, version='Remove Bak File')
   
    currentPath = os.getcwd().replace('\\','/') + '/'

    kwargs = {}
    dir = ''
    exts = ''
    silent = False         

    if not args['<dir>']:
        dir = currentPath
    else:
        dir = args['<dir>']
    
    if args['<exts>']:
        kwargs = {'dir':dir, 'exts':args['<exts>'], 'silent':args['-s'],'empty':args['-e']}
    else:
        kwargs = {'dir':dir,'silent':args['-s'],'empty':args['-e']} 
        
    removeBakFiles(**kwargs)

if __name__ == '__main__':
    main()



 