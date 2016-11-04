'''
Main monitor engine

It should include a collection of monitors

Author  : Adrian Tilita
Email   : adrian@tilita.ro
Created : 2016-10
Licence : (At the moment undecided)
'''
from abc import ABCMeta, abstractmethod
import importlib


class Monitor():
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

    def start(self):
        if len(self._availableMonitors) == 0:
            raise Exception("No available monitors builded!")

        result = {}
        for monitorName in self._availableMonitors:
            currentMonitor = self._availableMonitors[monitorName]
            result[monitorName] = currentMonitor.collectData()

        return result
