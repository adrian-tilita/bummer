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
Created : 2016-10-14
Modified: 2016-10-14
Licence : (At the moment undecided)
'''
import telnetlib
import re


def collectData(filters=None, config=None):
    '''
    Return memcached usage

    Args:
        filters (None|dict): Filter to monitor only parts of the component
        config (None|dict): Config data if necessary

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

    client = telnetlib.Telnet('127.0.0.1', 11211)
    client.write("stats\n")
    rawData = client.read_until('END')

    for key in acceptedFilters:
        if filters is not None and (filters[key] is not None and
                                    filters[key] is False):
            continue
        else:
            items = re.findall("STAT " + key + "(.*)\\r", rawData)
            if len(items) == 0:
                continue
            result[key] = items.pop().replace(" ", "")
    return result
