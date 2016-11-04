from monitors import memcache
from stubs.telnet_mock import MockedTelnet
#import monitors
import unittest
import mock


@mock.patch('telnetlib.Telnet', MockedTelnet())

class TestMemcacheMonitor(unittest.TestCase):
    def test_configInjection(self):
        '''This tests the monitor.type more than the memcachemonitor'''
        memcacheMonitor = memcache.MemcacheMonitor()
        givenHostname = 'dummy-hostname'
        givenPort = 221122
        with self.assertRaises(Exception):
            memcacheMonitor.collectData()
        memcacheMonitor.setConfig({'hostname': givenHostname,'port':givenPort})
        self.assertEqual(memcacheMonitor.getConfigByKey('hostname'), givenHostname, "Hostname given doesn't match with the one set")
        self.assertEqual(memcacheMonitor.getConfigByKey('port'), givenPort, "Port given doesn't match with the one set")

        print(memcacheMonitor.collectData())


if __name__ == '__main__':
    unittest.main()