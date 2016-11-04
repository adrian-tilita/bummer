class MockedTelnet():
    def __init__(self, host=None, port=0, timeout=None):
        pass

    def __call__(self, host=None, port=0, timeout=None):
        pass

    def write(self, buffer):
        pass

    def read_until(self, match, timeout=None):
        pass