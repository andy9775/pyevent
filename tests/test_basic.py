__author__ = 'andy'
import unittest

from pyevent import Pyevent


class PyeventTest(unittest.TestCase):
    def setUp (self):
        self.binderTwo = Pyevent()

    def tearDown (self):
        del self.binderTwo

    def test_bind (self):
        def test ():
            pass

        self.binderTwo.bind('test_bind', test)
        self.assertEqual(self.binderTwo._events['test_bind'][0], test,
                         'ensure binding')

    def test_trigger (self):
        self.boolean = False

        def change ():
            self.boolean = True

        self.binderTwo.bind('test_trigger', change)
        self.binderTwo.trigger('test_trigger')
        self.assertTrue(self.boolean, 'should change the value on trigger')

    def test_unbind (self):
        def test ():
            pass

        self.binderTwo.bind('test_unbind', test)
        self.assertEqual(self.binderTwo._events['test_unbind'][0], test)
        self.binderTwo.unbind('test_unbind', test)
        with self.assertRaises(KeyError):
            self.binderTwo._events['test_unbind']

    def test_multiple_callbacks (self):
        self.firstBoolean = False
        self.secondBoolean = False

        def first ():
            self.firstBoolean = True

        def second ():
            self.secondBoolean = True

        self.binderTwo.bind('test_multiple_callbacks', first)
        self.binderTwo.bind('test_multiple_callbacks', second)
        self.binderTwo.trigger('test_multiple_callbacks')
        self.assertTrue(self.firstBoolean, 'test first callback')
        self.assertTrue(self.secondBoolean, 'test second callback')


if __name__ == '__main__':
    unittest.main()
