from unittest import TestCase
from pizza import move_pizza

class PizzaTest(TestCase):

    def test_first_input(self):
        self.assertEqual(move_pizza('5x5 (1,3) (4,4)'), 'ENNNDEEEND')
    
    def test_second_input(self):
        with self.assertRaises(AttributeError):
            move_pizza(551344)
            
    def test_third_input(self):
        with self.assertRaises(SyntaxError):
            move_pizza('5x5 (1, 3) (4, 4)')
    
    def test_forth_input(self):
        self.assertEqual(move_pizza('5x5'), '')
    
    def test_fifth_input(self):
        self.assertEqual(move_pizza(''), '')
