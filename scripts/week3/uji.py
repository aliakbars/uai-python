import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.foo = 'foo'
        self.bar = 'BAR'

    def test_upper(self):
        self.assertEqual(self.foo.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue(self.bar.isupper())
        self.assertFalse(self.foo.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()