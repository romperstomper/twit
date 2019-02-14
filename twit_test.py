import twit

import unittest


class TestTwit(unittest.TestCase):
    def test_readtweets_pass(self):
        expected=False
        result = twit.readtweets()[1][:75]
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
