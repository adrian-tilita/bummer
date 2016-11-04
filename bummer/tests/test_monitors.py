from monitors import memcache
import unittest

class TestMemcacheMonitor(unittest.TestCase):
    def test_configNotSet(self):
        memcacheMonitor = memcache.MemcacheMonitor()
        self.assertRaises(Exception, memcacheMonitor.collectData())

if __name__ == '__main__':
    unittest.main()