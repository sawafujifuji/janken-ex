import unittest
from unittest.mock import patch
from source.computer import computer_pon

class TestComputerPon(unittest.TestCase):
    
    @patch('random.choice', return_value='グー')
    def test_guu_c(self, mock_random):
        self.assertEqual(computer_pon(), 'グー')
        
    @patch('random.choice', return_value='チョキ')
    def test_tyoki_c(self, mock_random):
        self.assertEqual(computer_pon(), 'チョキ')
        
    @patch('random.choice', return_value='パー')
    def test_paa_c(self, mock_random):
        self.assertEqual(computer_pon(), 'パー')