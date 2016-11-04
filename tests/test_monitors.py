#import monitor
#import monitors
#import sys
#import package_reference
#import bummer
#import bummer.monitor as monitor
#from bummer.monitor.monitors import memcache
#from package_reference import bummer.monitor.monitors as monitors
import unittest

class TestMemcacheMonitor(unittest.TestCase):
    def test_filterSet(self):
        #monitor = monitors.memcache.MemcacheMonitor()
        print(monitor.builder)
        print(memcache)
'''
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
'''
if __name__ == '__main__':
    unittest.main()