'''
This is just a test for working with the desired monitor
'''
from monitors import SystemMonitor, MemcacheMonitor

try:
    for i in range(0, 1):
        #print(SystemMonitor.collectData())
        print(MemcacheMonitor.collectData())
except KeyboardInterrupt:
    print ("Stopped!")