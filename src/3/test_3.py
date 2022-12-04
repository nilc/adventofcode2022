from unittest import TestCase
from solver import get_prio

class Test(TestCase):
    def test_get_prio(self):
        self.assertEqual(get_prio("A"),27)
