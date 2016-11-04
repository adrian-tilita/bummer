import importlib
from monitor.engine import Monitor
import monitor.type as MonitorType


def build(config):
    '''
    Return monitor.engine.Monitor
    '''
    monitor = Monitor()
    for key in config:
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
                    str("monitor.monitors." + key)
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
            if 'filters' in config[key]:
                filters = config[key]['filters']
            buildedMonitor.setFilters(filters)
        ''' if the class was builded, inject config '''
        if isinstance(buildedMonitor, MonitorType.ConfigAware) is True:
            configToSet = None
            if 'config' in config[key]:
                configToSet = config[key]['config']
            buildedMonitor.setConfig(configToSet)

        monitor.addMonitor(buildedMonitor)
    return monitor
