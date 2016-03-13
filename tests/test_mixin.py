__author__ = 'andy'
import unittest

from pyevent import mixin


@mixin
class TestClass:
    pass


class PyeventTest(unittest.TestCase):
    def setUp (self):
        self.cls = TestClass()

    def tearDown (self):
        del self.cls

    def test_mixin_build_trigger (self):
        self.assertIsNotNone(self.cls.trigger,
                             'ensure that trigger method is set')

    def test_mixin_build_bind (self):
        self.assertIsNotNone(self.cls.bind,
                             'ensure that bind method is set')

    def test_mixin_build_unbind (self):
        self.assertIsNotNone(self.cls.unbind,
                             'ensure that unbind method is set')

    def test_mixin_build_events (self):
        self.assertIsNotNone(self.cls._events,
                             'ensure that events dict is set')

    def test_mixin_bind (self):
        def go ():
            pass

        self.cls.bind('test_mixin_bind', go)
        self.assertEqual(self.cls._events['test_mixin_bind'][0], go,
                         'should bind the go function')

    def test_mixin_unbind (self):
        def go ():
            pass

        self.cls.bind('test_mixin_unbind', go)
        self.assertEqual(self.cls._events['test_mixin_unbind'][0], go)
        self.cls.unbind('test_mixin_unbind', go)
        with self.assertRaises(KeyError):
            self.cls._events['test_mixin_unbind']

    def test_mixin_trigger (self):
        self.boolean = False

        def go ():
            self.boolean = True

        self.cls.bind('test_mixin_trigger', go)
        self.cls.trigger('test_mixin_trigger')
        self.assertTrue(self.boolean, 'ensure value changed')

    def test_multiple_callbacks (self):
        self.booleanOne = False
        self.booleanTwo = False

        def one ():
            self.booleanOne = True

        def two ():
            self.booleanTwo = True

        self.cls.bind('test_multiple_callbacks', one)
        self.cls.bind('test_multiple_callbacks', two)
        self.cls.trigger('test_multiple_callbacks')
        self.assertTrue(self.booleanOne, 'ensure first value changed')
        self.assertTrue(self.booleanTwo, 'ensure second value changed')


if __name__ == '__main__':
    unittest.main()
