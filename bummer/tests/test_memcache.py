from monitors import memcache
from stubs.telnet_mock import MockedTelnet
import unittest
import mock


@mock.patch(
            'telnetlib.Telnet',
            MockedTelnet
        )
class TestMemcacheMonitor(unittest.TestCase):
    '''
    The MemcacheMonitor
    @todo - 
    '''
    expectedWriteArguments = None
    expectedReadResponse = None

    def setUp(self):
        memcacheMonitor = memcache.MemcacheMonitor()
        memcacheMonitor.setConfig(
            {
                'hostname': '127.0.0.1',
                'port': 11211
            }
        )
        self.instance = memcacheMonitor

    def test_collectData(self):
        '''
        Test memcache monitor collectData()

        We know that the order of the calls will be
        executed by MemcacheMonitor so we can "orchestrate"
        the response
        '''
        MockedTelnet.methodCallHandler = self
        self.expectedWriteArguments = "stats\n"
        '''Actual monitor functionality'''
        print (self.instance.collectData())

    def mockWriteResponse(self, buffer):
        '''Handle StubObject call for ::write'''
        self.assertEquals(
            self.expectedWriteArguments,
            buffer,
            "Expected <" + str(self.expectedWriteArguments) + "> -- received" +
            " <" + str(repr(buffer)) + ">"
        )

    def mockReadUntilResponse(self, match, timeout):
        '''Handle StubObject call for ::read_until'''
        print match
        print timeout
        print self.expectedReadResponse

if __name__ == '__main__':
    unittest.main()
