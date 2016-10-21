'''
Monitor Collection

A collection of injected monitors
and acts like a single monitor

Author  : Adrian Tilita
Email   : adrian@tilita.ro
Created : 2016-10
Modified: 2016-10-14
Licence : (At the moment undecided)
'''
from abc import ABCMeta, abstractmethod


class BaseMonitor():
    __metaclass__ = ABCMeta

    @abstractmethod
    def collectData(self):
        '''
        Force implementation for the current method in each monitor
        '''
        raise Exception(
            "Class %s does not have ::collectData method implemented"
            % self.__class__)
