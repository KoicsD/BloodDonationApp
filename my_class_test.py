__author__ = 'KoicsD'


class MethodToTest(object):
    def __init__(self, name, handle, is_static):
        self.name = name
        self.handle = handle
        self.is_static = is_static

    def invoke(self, obj):
        if self.is_static:
            self.handle()
        else:
            self.handle(obj)
