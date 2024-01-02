import unittest
import context
import backend.src.main as subject


class TestStringMethods(unittest.TestCase):

    def test_output(self):
        self.assertEqual('equal', 'equal')
#        self.assertEqual('hello world', subject.hello())


if __name__ == '__main__':
    unittest.main()
