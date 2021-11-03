from unittest.mock import patch
from unittest import TestCase


def get_input(text):
    hello = input(text)
    return hello


def answer():
    ans = get_input('enter yes or no')
    if ans == 'yes':
        return 'you entered yes'
    if ans == 'no':
        return 'you entered no'


class Test(TestCase):

    # get_input will return 'yes' during this test
    @patch('newer_test.get_input', return_value='yes')
    def test_answer_yes(self, hello):
        self.assertEqual('you entered yes', answer())

    @patch('newer_test.get_input', return_value='no')
    def test_answer_no(self, hello):
        self.assertEqual(answer(), 'you entered no')
