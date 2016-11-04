import sys
import os

'''Define the <bummer> package full path'''
bummerFullPath   = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
monitorFullPath  = os.path.join(bummerFullPath, 'monitor')
monitorsFullPath = os.path.join(monitorFullPath, 'monitors')

def load():
    '''Set the required packages to pythonpath'''
    sys.path.append(bummerFullPath)
    sys.path.append(monitorFullPath)
    sys.path.append(monitorsFullPath)

#if __name__ == '__main__':
load()