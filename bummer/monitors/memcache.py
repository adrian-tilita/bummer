'''
Memcache Monitor

Collect data from memcache server
    - Current number of connections
    - Bytes writen/read
    - Malloc Fails
    - Current Items
    - Get Count
    - Set Count
    - Get Misses
    - Delete Misses
* The list can be increased, currently I will deal with the data I need

Author  : Adrian Tilita
Email   : adrian@tilita.ro
Created : 2016-10
'''
import telnetlib
import re
import monitor.type as MonitorType


class MemcacheMonitor(
    MonitorType.BaseMonitor,
    MonitorType.FilterAware,
    MonitorType.ConfigAware
):
    '''
    Filters should be a disctionary with the key representig
    the filter and the value bool
    Ex: {'curr_connections': True, 'bytes_written': True, 'bytes_read': True}
    '''

    '''
    Available filters keys
    '''
    FILTER_CURRENT_CONNECTIONS = 'curr_connections'
    FILTER_BYTES_WRITTEN = 'bytes_written'
    FILTER_BYTES_READ = 'bytes_read'
    FILTER_ALLOCATION_FAILS = 'malloc_fails'
    FILTER_GET_COMMANDS = 'cmd_get'
    FILTER_GET_MISSES = 'get_misses'
    FILTER_SET_COMMANDS = 'cmd_set'
    FILTER_DELETE_MISSES = 'delete_misses'

    _acceptedFilters = []

    def setFilters(self, filters):
        '''
        Decorate parent to process the filters
        '''
        # Add to parent first
        super(MemcacheMonitor, self).setFilters(filters)
        for key in vars(MemcacheMonitor).keys():
            if key.find('FILTER_') == -1:
                continue
            currentKeyValue = getattr(self, key)
            if self.shouldExclude(currentKeyValue) is True:
                continue
            self._acceptedFilters.append(currentKeyValue)

    def collectData(self):
        '''
        Return memcached usage
        Returns:
            dict:   Returns a set of data of the form
                    {'curr_connections': int, 'bytes_written': int,
                        'bytes_read': int, 'malloc_fails': int,
                        'cmd_get': int, 'cmd_set': int, 'get_misses': int,
                        'delete_misses': int }
        '''
        if (
            self.getConfigByKey('hostname') is None or
            self.getConfigByKey('port') is None
        ):
            raise Exception("No hostname or port defined!")

        result = {}
        client = telnetlib.Telnet(
            self.getConfigByKey('hostname'),
            self.getConfigByKey('port')
        )
        client.write("stats\n")
        rawData = client.read_until('END')

        for key in self._acceptedFilters:
            '''
            if we cannot handle or find the specific filter
            we at least define it
            '''
            result[key] = '?'
            items = re.findall("STAT " + key + "(.*)\\r", rawData)
            if len(items) == 0:
                continue
            result[key] = items.pop().replace(" ", "")
        return result
