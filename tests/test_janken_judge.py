import unittest
from source.janken_judge import judge

class TestJudgeFunction(unittest.TestCase):
    def test_draw_guu(self):
        self.assertEqual(judge('グー', 'グー'), 'draw')

    def test_draw_paa(self):
        self.assertEqual(judge('パー', 'パー'), 'draw')

    def test_draw_tyoki(self):
        self.assertEqual(judge('チョキ', 'チョキ'), 'draw')

    def test_win_guu_p(self):
        self.assertEqual(judge('チョキ', 'グー'), 'player_win')
        
    def test_win_paa_p(self):
        self.assertEqual(judge('グー', 'パー'), 'player_win')
        
    def test_win_tyoki_p(self):
        self.assertEqual(judge('パー', 'チョキ'), 'player_win')

    def test_win_guu_c(self):
        self.assertEqual(judge('グー', 'チョキ'), 'computer_win')
        
    def test_win_paa_c(self):
        self.assertEqual(judge('パー', 'グー'), 'computer_win')
        
    def test_win_tyoki_c(self):
        self.assertEqual(judge('チョキ', 'パー'), 'computer_win')

if __name__ == '__main__':
    unittest.main()




