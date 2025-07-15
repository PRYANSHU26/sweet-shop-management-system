import unittest
import sys
import os

# Add path to sweetshop.py
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

    def test_view_sweets(self):
        shop = SweetShop()
        shop.add_sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
        shop.add_sweet(1002, "Gajar Halwa", "Vegetable-Based", 30, 15)
        sweets = shop.view_sweets()
        self.assertEqual(len(sweets), 2)
        self.assertEqual(sweets[0]['name'], "Kaju Katli")
        self.assertEqual(sweets[1]['name'], "Gajar Halwa")

    def test_search_by_name(self):
        shop = SweetShop()
        shop.add_sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
        shop.add_sweet(1002, "Gajar Halwa", "Vegetable-Based", 30, 15)
        results = shop.search_sweets(name="Kaju Katli")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['id'], 1001)

    def test_search_by_category(self):
        shop = SweetShop()
        shop.add_sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
        shop.add_sweet(1002, "Gajar Halwa", "Vegetable-Based", 30, 15)
        shop.add_sweet(1003, "Badam Barfi", "Nut-Based", 40, 10)
        results = shop.search_sweets(category="Nut-Based")
        self.assertEqual(len(results), 2)

    def test_search_by_price_range(self):
        shop = SweetShop()
        shop.add_sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
        shop.add_sweet(1002, "Gajar Halwa", "Vegetable-Based", 30, 15)
        shop.add_sweet(1003, "Rasgulla", "Milk-Based", 10, 25)
        results = shop.search_sweets(price_min=20, price_max=40)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['name'], "Gajar Halwa")

    def test_sort_by_name(self):
        shop = SweetShop()
        shop.add_sweet(1002, "Gajar Halwa", "Vegetable-Based", 30, 15)
        shop.add_sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
        shop.add_sweet(1003, "Rasgulla", "Milk-Based", 10, 25)
        sorted_sweets = shop.sort_sweets(by="name")
        self.assertEqual(sorted_sweets[0]['name'], "Gajar Halwa")
        self.assertEqual(sorted_sweets[2]['name'], "Rasgulla")

    def test_sort_by_price_descending(self):
        shop = SweetShop()
        shop.add_sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
        shop.add_sweet(1002, "Gajar Halwa", "Vegetable-Based", 30, 15)
        shop.add_sweet(1003, "Rasgulla", "Milk-Based", 10, 25)
        sorted_sweets = shop.sort_sweets(by="price", descending=True)
        self.assertEqual(sorted_sweets[0]['price'], 50)
        self.assertEqual(sorted_sweets[2]['price'], 10)

if __name__ == '__main__':
    unittest.main()
