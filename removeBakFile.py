#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Usage:
  removeBakFile.py [-s]
  removeBakFile.py dir <dir> [<exts>] [-s]
  removeBakFile.py <exts> [-s]


Options:
  -h --help     Show this screen
  -s            silent remove
  dir           dir, if none use current dir
  exts          bakfile ext. if none default 'bak'. more ext:'bak,bak2,...'
"""


import os
import os.path
from docopt import docopt

def getFileList(dir):
    fileList = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            filePath = root + '/' + name
            filePath = filePath.replace('\\','/')
            fileList.append(filePath)
    return fileList

def grepList(fileList,exts=['bak']):
    targetList =[]
    for filePath in fileList:
        ext = filePath.split('.')[-1]
        if ext in exts:
            targetList.append(filePath)
    return targetList

def removeBakFiles(dir,exts=[],silent=False):
    if len(exts):
        exts = exts.split(',')
        targetList = grepList(getFileList(dir),exts)
    else:
        targetList = grepList(getFileList(dir))
    
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
        kwargs = {'dir':dir, 'exts':args['<exts>'], 'silent':args['-s']}
    else:
        kwargs = {'dir':dir,'silent':args['-s']} 
        
    removeBakFiles(**kwargs)

if __name__ == '__main__':
    main()



 