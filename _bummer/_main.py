'''
This is just a test for working with the desired monitor
'''
from monitor.Monitor import MonitorBuilder
#from monitor.MemcacheMonitor import MemcacheMonitor
from sender import File

config = {
    MonitorBuilder.MEMCACHE: {
        'config': {"hostname": "127.0.0.1", "port": 11211},
        'filters': None
    }
}
print (MonitorBuilder.MEMCACHE)
'''
'''
'''

MonitorBuilder.SYSTEM: {
    'filters': {
        'cpu': False,
        'memory': False
    }
}

builder = MonitorBuilder()
monitor = builder.build(config)
writer = File.FileWriter()
item = 0
while item < 1:
    item = item+1
#    print(monitor.collectData())
    writer.sendMessage(monitor.collectData())
'''
