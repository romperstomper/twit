import twit

import unittest
from unittest.mock import Mock, patch


class TestTwit(unittest.TestCase):
    @patch('twit.twitter.Api.GetUserTimeline', return_value=['fake', 'tweets'])
    def test_readtweets_pass(self, mock_timeline):
        expected = ['fake', 'tweets']
        result = twit.readtweets()
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
