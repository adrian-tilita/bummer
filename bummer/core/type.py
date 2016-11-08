'''
Monitor structure types definitions:

::BaseMonitor - AbstractMonitor definition
::FilterAware - Defines the property that a monitor
                can be aware of filters that establish
                what parts of the monitor capabilities
                should be included
::ConfigAware - Defines the property that a monitor
                can be aware of config parameters
                such as hostnames, ports etc

Author  : Adrian Tilita
Email   : adrian@tilita.ro
Created : 2016-10
'''
from abc import ABCMeta, abstractmethod


class BaseMonitor():
    '''
    Defines a structure for the
    monitor definition
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def collectData(self):
        '''
        Force implementation for the current method in each monitor
        '''
        raise Exception(
            "Class %s does not have ::collectData method implemented"
            % self.__class__)


class FilterAware():
    '''
    Establish filter aware monitor,
    adding the posibility for a monitor
    to support filters
    '''
    __metaclass__ = ABCMeta

    '''
    The injected filters
    '''
    _filters = None

    def setFilters(self, filters):
        '''
        Inject the required filters
        '''
        self._filters = filters

    def shouldExclude(self, filterKey):
        '''
        Validate the filters by key, actually make
        the repeating validation if key exists, if key
        has a value and so on
        Return:
            bool
        '''
        if (
            self._filters is not None and
            filterKey in self._filters and
            self._filters[filterKey] is False
           ):
            return True
        '''
        if the conditions above are not met
        we assume that the current filter
        is not active
        '''
        return False


class ConfigAware():
    '''
    Establish config aware monitor,
    adding the posibility for a monitor
    to support config parameters
    '''
    __metaclass__ = ABCMeta

    '''
    The injected config
    '''
    _config = None

    def setConfig(self, config):
        '''
        Inject the required config data
        '''
        self._config = config

    def getConfigByKey(self, requestedConfigKey):
        '''
        Get the key if we have it in the config
        If not, we return None
        '''
        if (
            self._config is not None and
            requestedConfigKey in self._config
           ):
            return self._config[requestedConfigKey]
        return None
