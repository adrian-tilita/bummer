'''
Monitor Builder

It creates the Monitor Engine,
add monitors builded based on the
given config and add them to Monitor Engine
and returns it

Author  : Adrian Tilita
Email   : adrian@tilita.ro
Created : 2016-10
Licence : (At the moment undecided)
'''
import importlib
from core.engine import Monitor
import core.type as MonitorType


def build(config):
    '''
    Return monitor.engine.Monitor
    '''
    monitorEngine = Monitor()
    monitorsConfig = config['monitors']
    for key in monitorsConfig:
        try:
            '''
            Dinamically load a monitor based on the requested
            config parameters. Any config key is the representation
            of the monitor name.
            Example:
            key - mysql -> should refer to
                monitor.monitors.mysql.MysqlMonitor
            @todo - Implement underscore - camelcase conversion
            '''
            className = key[0].upper() + key[1:] + "Monitor"
            class_ = getattr(
                importlib.import_module(
                    str("monitors." + key)
                ), className
            )
            buildedMonitor = class_()
        except Exception as e:
            print(e)
            print("Cannot load " + className + " from monitor." + key)
            continue
        ''' if the class was builded, inject filters '''
        if isinstance(buildedMonitor, MonitorType.FilterAware) is True:
            '''
            We still try to set filters
            event if no filter isset - so we can
            further support decoration
            '''
            filters = None
            if 'filters' in monitorsConfig[key]:
                filters = monitorsConfig[key]['filters']
            buildedMonitor.setFilters(filters)
        ''' if the class was builded, inject config '''
        if isinstance(buildedMonitor, MonitorType.ConfigAware) is True:
            configToSet = None
            if 'config' in monitorsConfig[key]:
                configToSet = monitorsConfig[key]['config']
            buildedMonitor.setConfig(configToSet)

        monitorEngine.addMonitor(buildedMonitor)
    return monitorEngine
