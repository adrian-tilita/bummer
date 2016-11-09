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
import threading
import syslog


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
        ''' Send collected data to available notifiers '''
        if len(self._availableNotifiers) == 0:
            print "Collected data"# (str(identifier) + "<--->: " + str(message))
            return
        for notifier in self._availableNotifiers:
            self._availableNotifiers[notifier].pushNotification(message, identifier)

    def start(self):
        ''' Start monitors and notify with collected data '''
        if len(self._availableMonitors) == 0:
            raise Exception("No available monitors builded!")
        self.started = True
        ''' Start decoupled from the current thread '''
        thread = threading.Thread(target=self._collectData)
        thread.start()
        syslog.syslog('Monitor start request caught')
        return True

    def _collectData(self):
        ''' Collect data from monitor and forward it to the notifiers '''
        while self.started is True:
            for monitorName in self._availableMonitors:
                currentMonitor = self._availableMonitors[monitorName]
                self.pushNotification(currentMonitor.collectData(), monitorName)        
        
    def stop(self):
        ''' Stop monitoring '''
        syslog.syslog('Monitor stop request caught')
        self.started = False
        
