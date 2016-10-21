'''
General Monitor

It should include a collection of monitors

Author  : Adrian Tilita
Email   : adrian@tilita.ro
Created : 2016-10
Licence : (At the moment undecided)
'''
from BaseMonitor import BaseMonitor


class Monitor(BaseMonitor):
    '''
    Should contain all de builded monitors
    '''
    _availableMonitors = {}

    def addMonitor(self, buildedMonitor):
        '''
        Add a monitor into the list
        Arguments:
            buildedMonitor  - A baseMonitor instance
        '''
        self._availableMonitors[type(buildedMonitor).__name__] = buildedMonitor

    def removeMonitor(self, monitorAlisName):
        '''
        Removes a monitor from list
        Arguments:
            buildedMonitor  - A baseMonitor instance
        '''
        if self._availableMonitors[monitorAlisName] is not None:
            del self._availableMonitors[monitorAlisName]

    def collectData(self):
        if len(self._availableMonitors) == 0:
            raise Exception("No available monitors builded!")

        result = {}
        for monitorName in self._availableMonitors:
            result[monitorName] = self._availableMonitors[monitorName].collectData()

        return result
