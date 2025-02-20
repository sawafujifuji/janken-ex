import unittest
from unittest.mock import patch, Mock

import sys
sys.path.append(r"C:\Users\sawafuji\OneDrive\Desktop\アジャイル開発\janken-ex\source")
from computer import computer_pon


class TestComputer(unittest.TestCase):
    def test_computer_pon_returns_valid_hand(self):
        valid_hands = ["グー", "チョキ", "パー"]
        result = computer_pon()
        self.assertIn(result, valid_hands)

    @patch('random.choice', return_value='グー')
    def test_computer_pon_uses_random_choice(self, mock_choice):
        result = computer_pon()
        self.assertEqual(result, 'グー')
        mock_choice.assert_called_once()

if __name__ == '__main__':
    unittest.main()