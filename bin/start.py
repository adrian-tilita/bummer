import sys


def showHelp():
    '''
    Show de console help
    '''
    print ("Usage: start.py -t [type]")
    print ("-t [type] \t: Start mode type: master / slave")
    

if len(sys.argv) == 1 or (
    len(sys.argv) == 2 and (
            sys.argv[1] == '-h' or
            sys.argv[1] == '--help' or
            sys.argv[1] == '?'
        )
    ):
    showHelp()
else:
    
    print (sys.argv)
