import unittest
from tictactoe import Board

class TestBoard(unittest.TestCase):
   
    def test_mark_square(self):        
        b=Board()
        self.assertTrue(b.mark_square(0,1,'X'))
        self.assertFalse(b.mark_square(0,1,0))
        self.assertFalse(b.mark_square(0,'X','X'))
        self.assertFalse(b.mark_square('X',1,'X'))
        self.assertFalse(b.mark_square('X','X','X'))
        self.assertFalse(b.mark_square(0,'X',0))
        self.assertFalse(b.mark_square('X',1,0))
        self.assertFalse(b.mark_square('X','X','X'))
        b1 = Board()
        b1.mark_square(0,0,'X')
        self.assertFalse(b1.mark_square(0,0,'X'))
    
    def test_has_winner(self):
        b=Board()
        b.mark_square(0,0,'X')
        b.mark_square(0,1,'X')
        b.mark_square(0,2,'O')
        self.assertFalse(b.has_winner())
        b.mark_square(1,0,'X')
        b.mark_square(2,0,'X')
        self.assertTrue(b.has_winner())

if __name__ == '__main__':
    unittest.main()
