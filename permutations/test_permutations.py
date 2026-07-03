import unittest
from permutations import countSmileys

class TestCountSmileys(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(countSmileys([':)', ';(', ';}', ':-D']), 2)

    def test_example_2(self):
        self.assertEqual(countSmileys([';D', ':-(', ':-)', ';~)']), 3)

    def test_example_3(self):
        self.assertEqual(countSmileys([';]', ':[', ';*', ':$', ';-D']), 1)

    def test_empty_array(self):
        self.assertEqual(countSmileys([]), 0)

if __name__ == '__main__':
    unittest.main()