'''
Notifier Base Type

Author  : Adrian Tilita
Email   : adrian@tilita.ro
Created : 2016-11
'''
from abc import ABCMeta, abstractmethod


class BaseNotifier():
    '''
    Defines a structure for the
    monitor definition
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def push(self, message):
        '''
        Force implementation for the current method in each notifier
        '''
        raise Exception(
            "Class %s does not have ::push method implemented"
            % self.__class__)
