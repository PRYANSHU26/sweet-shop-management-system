import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sweetshop import SweetShop

class TestSweetShop(unittest.TestCase):

    def test_add_sweet(self):
        shop = SweetShop()
        shop.add_sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
        self.assertEqual(len(shop.inventory), 1)
        self.assertEqual(shop.inventory[0]['name'], "Kaju Katli")

    def test_delete_sweet(self):
        shop = SweetShop()
        shop.add_sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
        shop.add_sweet(1002, "Gajar Halwa", "Vegetable-Based", 30, 15)

        shop.delete_sweet(1001)

        self.assertEqual(len(shop.inventory), 1)
        self.assertEqual(shop.inventory[0]['id'], 1002)

if __name__ == '__main__':
    unittest.main()
