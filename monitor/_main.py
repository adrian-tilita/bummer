'''
This is just a test for working with the desired monitor
'''
from MonitorBuilder import MonitorBuilder


config = {
    MonitorBuilder.MEMCACHE: {
        'config': {"hostname": "127.0.0.1", "port": 11211},
        'filters': None
    },
    MonitorBuilder.SYSTEM: {
        'filters': None
    }
}

builder = MonitorBuilder()
monitor = builder.build(config)
print (monitor)