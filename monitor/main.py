'''
This is just a test for working with the desired monitor
'''
from monitors import SystemMonitor

try:
    for i in range(0, 20):
        print(SystemMonitor.collectData())
except KeyboardInterrupt:
    print ("Stopped!")