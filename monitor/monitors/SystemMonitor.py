'''
System Monitors

Collect system relevent information like:
    - CPU Usage
    - Memory Usage
    - Swap Memory*
    - Disk IO
    - Network Traffic
* Needs implementation

Author  : Adrian Tilita
Email   : adrian@tilita.ro
Created : 2016-10-04
Modified: 2016-10-04
Licence : (At the moment undecided)
'''
import psutil


def collectData(filters=None, config = None):
    '''
    Return system usage

    Args:
        filters (None|dict): Filter to monitor only parts of the component

    Returns:
        dict:   Returns a set of data of the form
                {'cpu_usage':
                    {'per_cpu':double,'total':double},
                 'memory':
                    {'total':double,'used':double,'percent':double}
                }
    '''

    result = {}
    '''
    Collect CPU data
    '''
    if filters is None or (filters['cpu'] is not None and filters['cpu'] is not False):
        result['cpu_usage'] = {}
        result['cpu_usage']['per_cpu'] = psutil.cpu_percent(interval=0.4,
                                                            percpu=True)
        result['cpu_usage']['total'] = psutil.cpu_percent(interval=0.4,
                                                          percpu=False)

    '''
    Collect Memory usage

    memory_usage:
        0 => total,
        1 => available,
        2 => percent,
        3 => used,
        4 => free
    '''
    if filters is None or (filters['memory'] is not None and filters['memory'] is not False):
        result['memory'] = {}
        memory_usage = psutil.virtual_memory()
        result['memory']['total'] = memory_usage[0]
        result['memory']['used'] = memory_usage[3]
        result['memory']['percent'] = memory_usage[2]

    '''
    Collect Disk IO

    read_count / write_count / read_bytes / write_bytes / read_time / write_time
    '''
    if filters is None or (filters['disk_io'] is not None and filters['disk_io'] is not False):
        result['disk_io'] = psutil.disk_io_counters(True)

    '''
    Collect network data
    
    bytes_sent / bytes_recv / packets_sent / packets_recv / errin / errout / dropin / dropout
    '''
    if filters is None or (filters['net_io'] is not None and filters['net_io'] is not False):
        result['net_io'] = psutil.net_io_counters(True)

    return result
