## I have tried with this code but I just cannot get it to work whatsoever,
### How does it work I'm so confuded and sure the code should work??
#It was working at one point but now it just won't work at all and I have gone back through my stepes to when It was working and it just wont work now.

import unittest
from shop import NotEnoughMoneyError, purchase_item

class TestShop(unittest.TestCase):
    def test_purchase_item_success(self):
        # Test purchasing an item when there is enough money
        global money
        global purchased
        money = 100
        purchased = False
        purchase_item('Croissant')
        self.assertTrue(purchased)
        self.assertEqual(money, 50)

    def test_purchase_item_not_enough_money(self):
        # Test purchasing an item when there is not enough money
        global money
        global purchased
        money = 40
        purchased = False
        with self.assertRaises(NotEnoughMoneyError):
            purchase_item('Brie')
        self.assertFalse(purchased)
        self.assertEqual(money, 40)

    def test_purchase_item_invalid_choice(self):
        # Test purchasing an invalid item choice
        global money
        global purchased
        money = 100
        purchased = False
        purchase_item('InvalidItem')
        self.assertFalse(purchased)
        self.assertEqual(money, 100)

    def test_purchase_item_additional_money(self):
        # Test purchasing an item after giving additional money
        global money
        global purchased
        money = 40
        purchased = False
        # Mock user input
        original_input = __builtins__.input
        __builtins__.input = lambda _: 'Y'
        purchase_item('Lemon')
        self.assertTrue(purchased)
        self.assertEqual(money, 15)
        __builtins__.input = original_input

    def test_purchase_item_no_additional_money(self):
        # Test purchasing after no additional money
        global money
        global purchased
        money = 40
        purchased = False
        # Mock user input
        original_input = __builtins__.input
        __builtins__.input = lambda _: 'N'
        purchase_item('Lemon')
        self.assertFalse(purchased)
        self.assertEqual(money, 40)
        __builtins__.input = original_input

if __name__ == '__main__':
    unittest.main()
