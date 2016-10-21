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
Licence : (At the moment undecided)
'''
import telnetlib
import re
from BaseMonitor import BaseMonitor


class MemcacheMonitor(BaseMonitor):
    '''
    Filters should be a disctionary with the key representig
    the filter and the value bool
    Ex: {'curr_connections': True, 'bytes_written': True, 'bytes_read': True}
    '''
    _filters = None

    '''
    Config should be a disctionary with hostname and port
    used for the connection to memcache from telnet
    '''
    _config = {"hostname": "127.0.0.1", "port": 11211}

    def __init__(self, filters=None, config=None):
        '''
        See @_filters and @_config
        '''
        if filters is not None:
            self._filters = filters
        if config is not None:
            if config["hostname"] is not None:
                self._config["hostname"] = config["hostname"]
            if config["port"] is not None:
                self._config["port"] = config["port"]

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
        result = {}

        acceptedFilters = {'curr_connections', 'bytes_written', 'bytes_read',
                           'malloc_fails', 'cmd_get', 'cmd_set', 'get_misses',
                           'delete_misses'}

        client = telnetlib.Telnet(
            self._config['hostname'],
            self._config['port'])
        client.write("stats\n")
        rawData = client.read_until('END')

        for key in acceptedFilters:
            if self._filters is not None and (
                self._filters[key] is not None and
                self._filters[key] is False
            ):
                continue
            else:
                # if we cannot handle or find the specific filter we at least define it
                result[key] = '?'; 
                items = re.findall("STAT " + key + "(.*)\\r", rawData)
                if len(items) == 0:
                    continue
                result[key] = items.pop().replace(" ", "")
        return result
