import sys
import re
import os
import commands

def analyse():
    fSrc = open(sys.argv[1], 'r')
    fDes = open(sys.argv[1] + '.t', 'w+')
    #while True:
    #line = fSrc.readline()
    lines = fSrc.readlines()
    print(lines)
    for line in lines:
        print(line)
        print('-----------------')
        line = line.replace('DEST', '')
        line = line.replace('=', '')
        line = line.replace(' ', '')
        line = line.replace('\n', '')
        params = line.split(':')
        print(params)
        print('===============')
        if params.__sizeof__() > 1:
            filePath = params[0]
            print(filePath)
            libName = '=================lib'+ params[1] + 'D.so=================\n'
            print(libName)
            fDes.write(libName)
            fDes.write(filePath + '\n')
            fDes.flush()
        shellCmd = 'grep BUILDTYPE ' + filePath
        dependLibs = commands.getoutput(shellCmd)
        print(dependLibs)
        print('++++++++++++++++++++++++++++++++++++')
        dependLibs = dependLibs.split()
        print(dependLibs)
        for lib in dependLibs:
            m = re.match('#', lib)
            if m is not None:
                continue
            m = lib.find('$(BUILDTYPE)', 1)
            print(lib)
            print('*********************')
            if m > 0:
                print('$$$$$$$$$$$$')
                print(lib)
                lib = lib.replace('\\', '')
                lib = 'lib' + lib.replace('$(BUILDTYPE)', 'D.so') + '\n'
                print(lib)
                fDes.write(lib)
                fDes.flush()

    fSrc.close()
    fDes.close()
if __name__ == "__main__":
    analyse()