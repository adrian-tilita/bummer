'''
System Monitor

Collect system relevent information like:
    - CPU Usage
    - Memory Usage
    - Swap Memory*
    - Disk IO
    - Network Traffic
* Needs implementation

Author  : Adrian Tilita
Email   : adrian@tilita.ro
Created : 2016-10
'''
import psutil
import core.type as MonitorType


class SystemMonitor(MonitorType.BaseMonitor, MonitorType.FilterAware):
    '''
    Available filters keys
    '''
    FILTER_CPU = 'cpu'
    FILTER_MEMORY = 'memory'
    FILTER_DISK_IO = 'disk_io'
    FILTER_NET_IO = 'net_io'

    def collectData(self):
        '''
        Return system usage
        Returns:
            dict:   Returns a set of data of the form
                    {'cpu_usage':
                        {'per_cpu':double,'total':double},
                     'memory':
                        {'total':double,'used':double,'percent':double}
                     'disk_io':
                        {TO DO}
                     'net_io':
                        {TO DO}
                    }
        '''
        result = {}
        '''
        Collect CPU data
         - per_cpu
         - total
        '''
        if self.shouldExclude(self.FILTER_CPU) is False:
            result[self.FILTER_CPU] = {}
            result[self.FILTER_CPU]['per_cpu'] = psutil.cpu_percent(
                interval=0.4,
                percpu=True)
            result[self.FILTER_CPU]['total'] = psutil.cpu_percent(
                interval=0.4,
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
        if self.shouldExclude(self.FILTER_MEMORY) is False:
            result[self.FILTER_MEMORY] = {}
            memory_usage = psutil.virtual_memory()
            result[self.FILTER_MEMORY]['total'] = memory_usage[0]
            result[self.FILTER_MEMORY]['used'] = memory_usage[3]
            result[self.FILTER_MEMORY]['percent'] = memory_usage[2]

        '''
        Collect Disk IO

        read_count / write_count / read_bytes / write_bytes /
        read_time / write_time
        '''
        if self.shouldExclude(self.FILTER_DISK_IO) is False:
            result[self.FILTER_DISK_IO] = self._convertNamedTupleToDic(
                psutil.disk_io_counters(True)
            )

        '''
        Collect network data

        bytes_sent / bytes_recv / packets_sent / packets_recv /
        errin / errout / dropin / dropout
        '''
        if self.shouldExclude(self.FILTER_NET_IO) is False:
            result[self.FILTER_NET_IO] = self._convertNamedTupleToDic(
                psutil.net_io_counters(True)
            )
        return result

    def _convertNamedTupleToDic(self, psUtilResult):
        '''
        psutil returns a dictionary
        containing namedtuples so we convert
        them to dictionary for later usage
        '''
        response = {}
        for itemIndex in psUtilResult:
            namedTupleToDic = psUtilResult[itemIndex]._asdict()
            response[itemIndex] = namedTupleToDic
        return response
