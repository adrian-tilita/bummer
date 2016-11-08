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
    _availableNotifiers = {}
    started = False

    def addMonitor(self, buildedMonitor):
        '''
        Add a monitor into the list
        Arguments:
            buildedMonitor  - A baseMonitor instance
        '''
        self._availableMonitors[type(buildedMonitor).__name__] = buildedMonitor

    def removeMonitor(self, monitorAliasName):
        '''
        Removes a monitor from list
        Arguments:
            buildedMonitor  - A baseMonitor instance
        '''
        if self._availableMonitors[monitorAliasName] is not None:
            del self._availableMonitors[monitorAliasName]

    def addNotifier(self, notifier):
        '''
        Add a notifier to the engine's list
        Arguments:
            notifier  - A BaseNotifier instance
        '''
        self._availableNotifiers[type(notifier).__name__] = notifier

    def pushNotification(self, message, identifier = None):
        print (str(identifier) + "<--->: " + str(message))

    def start(self):
        if len(self._availableMonitors) == 0:
            raise Exception("No available monitors builded!")
        self.started = True

        while self.started is True:
            for monitorName in self._availableMonitors:
                currentMonitor = self._availableMonitors[monitorName]
                self.pushNotification(currentMonitor.collectData(), monitorName)

    def stop(self):
        self.started = False
        
