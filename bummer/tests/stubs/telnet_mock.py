class MockedTelnet():
    '''
    We orchestrate the method calls so
    we can include them in testing scenarios
    '''
    methodCallHandler = None

    def __init__(self, host=None, port=0, timeout=None):
        self.instance = self

    def __call__(self, host=None, port=0, timeout=None):
        pass

    def write(self, buffer):
        '''Forward the call to the TestClass - TestMemcacheMonitor'''
        MockedTelnet.methodCallHandler.mockWriteResponse(buffer)
        return

    def read_until(self, match, timeout=None):
        '''Forward the call to the TestClass - TestMemcacheMonitor'''
        return MockedTelnet.methodCallHandler.mockReadUntilResponse(
            match, timeout
        )
