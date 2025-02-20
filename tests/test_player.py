
import unittest
from unittest.mock import patch
from source.player import player_pon

class TestPlayerModule(unittest.TestCase):

    @patch('builtins.input', return_value='1')
    def test_guu(self, mock_input):
        self.assertEqual(player_pon(), 'グー')
        
    @patch('builtins.input', return_value='2')
    def test_tyoki(self, mock_input):
        self.assertEqual(player_pon(), 'チョキ')
        
    @patch('builtins.input', return_value='3')
    def test_paa(self, mock_input):
        self.assertEqual(player_pon(), 'パー')
        
    @patch('builtins.input', return_value='0')
    def test_error(self, mock_input):
        with patch('builtins.input', side_effect=['0', '1']):  
            self.assertEqual(player_pon(), 'グー')
        
    @patch('builtins.input', return_value='4')
    def test_error2(self, mock_input):
        with patch('builtins.input', side_effect=['4', '2']): 
            self.assertEqual(player_pon(), 'チョキ')