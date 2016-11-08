from core import type
import unittest


class TestFilterAware(unittest.TestCase):
    '''Tests type.FilterAware'''

    '''FilterAware Instance'''
    classInstance = None

    '''Filters set'''
    filters = {
        'dummyFilter': False,
        'anotherFilter': None,
        'thirdFilter': True
    }

    def setUp(self):
        '''Build the FilterAware Instance'''
        self.classInstance = type.FilterAware()
        self.classInstance.setFilters(self.filters)

    def test_setFilters(self):
        '''
        Test that what is injected is set correctly
        in class members
        '''
        self.assertNotEqual(
            self.classInstance._filters,
            None,
            "No filters are set"
        )
        self.assertEquals(
            self.classInstance._filters,
            self.filters,
            "Injected filters are not handled correctly"
        )

    def test_shouldExclude(self):
        '''
        Test that a should exclude condition is handled
        correctly
        '''
        expectedAsserts = [
            {
                'key': 'dummyFilter',
                'result': True
            },
            {
                'key': 'anotherFilter',
                'result': False
            },
            {
                'key': 'thirdFilter',
                'result': False
            },
            {
                'key': 'undefinedFilter',
                'result': False
            }
        ]
        for assertItem in expectedAsserts:
            failMesssage = (
                "Injected filter <" +
                assertItem['key'] +
                "> is not correctly treated"
            )
            testResult = self.classInstance.shouldExclude(assertItem['key'])
            if assertItem['result'] is True:
                self.assertTrue(testResult, failMesssage)
            elif assertItem['result'] is False:
                self.assertFalse(testResult, failMesssage)
        '''Exclude on None filter'''
        self.classInstance.setFilters(None)
        self.assertFalse(
            self.classInstance.shouldExclude('anyKey'),
            "When no filters are injected no key should be excluded"
        )


class TestConfigAware(unittest.TestCase):
    '''Tests type.ConfigAware'''

    '''ConfigAware Instance'''
    classInstance = None

    '''Config parameters'''
    config = {
        'configKey1': 'Config value',
        'configKey2': False,
        'configKey3': True,
        'configKey4': None
    }

    def setUp(self):
        '''Build the ConfigAware Instance'''
        self.classInstance = type.ConfigAware()
        self.classInstance.setConfig(self.config)

    def test_getConfigKey(self):
        '''
        Test that what is injected is set correctly
        in class members
        '''
        self.assertNotEqual(
            self.classInstance._config,
            None,
            "Config values should not be empty"
        )
        self.assertEquals(
            self.classInstance._config,
            self.config,
            "Injected config is handled correctly"
        )

    def test_getConfigByKey(self):
        '''
        Test that a key existence
        is handled correctly
        '''
        for key in self.config:
            self.assertEqual(
                self.classInstance.getConfigByKey(key),
                self.config[key],
                (
                   "Injected config value <" +
                   key +
                   "> is not correctly treated"
                )
            )
        self.assertEqual(
            self.classInstance.getConfigByKey('NonExistingKey'),
            None,
            "A non-existing key should return None"
        )


class ExtendedDummyMonitor(type.BaseMonitor):
    '''Dummy instances that implements BaseMonitor'''
    def __init__(self):
        pass


class ExtendedDummyMonitorExceptionTest(type.BaseMonitor):
    '''Dummy instances that implements BaseMonitor'''
    def collectData(self):
        super(ExtendedDummyMonitorExceptionTest, self).collectData()


class TestBaseMonitor(unittest.TestCase):
    '''Tests type.BaseMonitor'''

    def test_instance(self):
        '''
        Test that the method throws exception
        when not implemented
        '''
        with self.assertRaises(TypeError):
            ExtendedDummyMonitor()

    def test_exception(self):
        '''
        Test that the method throws exception
        when not implemented
        '''
        with self.assertRaises(Exception):
            classInstance = ExtendedDummyMonitorExceptionTest()
            classInstance.collectData()


if __name__ == '__main__':
    unittest.main()
