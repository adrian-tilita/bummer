import sys
from communication import Udp


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
    if sys.argv[2] == 'master':
        print ("Run as master")
        sender = Udp.Sender("127.0.0.1", 5002)
        while True:
            sender.sendMessage("A message test")
    elif sys.argv[2] == 'slave':
        listener = Udp.Listener("127.0.0.1", 5002)
        listener.start()
        print ("Run as slave")
