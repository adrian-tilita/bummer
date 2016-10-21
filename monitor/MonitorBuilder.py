'''
Monitor Builder

Builds a monitor with monitors based on a dictionary config

Author  : Adrian Tilita
Email   : adrian@tilita.ro
Created : 2016-10
Licence : (At the moment undecided)
'''
from monitors.Monitor import Monitor
from monitors.MemcacheMonitor import MemcacheMonitor
from monitors.SystemMonitor import SystemMonitor


class MonitorBuilder():
    '''
    Defined monitor aliases
    '''
    MEMCACHE = 'MemcacheMonitor'
    SYSTEM = 'SystemMonitor'

    def build(self, config):
        # Should refactor for a more dinamic building
        monitor = Monitor()

        # Builds MemcacheMonitor
        if config[self.MEMCACHE] is not None:
            configParameter = None
            configFilters = None
            if config[self.MEMCACHE]['config'] is not None:
                configParameter = config[self.MEMCACHE]['config']
            if config[self.MEMCACHE]['filters'] is not None:
                configFilters = config[self.MEMCACHE]['filters']
            buildedMonitor = MemcacheMonitor(configFilters, configParameter)
            monitor.addMonitor(buildedMonitor)
        # Builds SystemMonitor
        if config[self.SYSTEM] is not None:
            configFilters = None
            if config[self.SYSTEM]['filters'] is not None:
                configFilters = config[self.SYSTEM]['filters']
            buildedMonitor = SystemMonitor(configFilters)
            monitor.addMonitor(buildedMonitor)

        return monitor
