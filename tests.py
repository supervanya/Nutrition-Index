import unittest
from interractive import *

class TestAPI(unittest.TestCase):

    def test_nutriet(self):
        food = Food(14555)

        self.assertEqual(food.index, -50)
        self.assertEqual(food.data[301]['value'], 10.0)
        self.assertEqual(food.data[304]['value'], 2.0)
        self.assertEqual(food.name, "Water, bottled, generic")

    def test_nutriet2(self):
        food = Food(19375)

        self.assertEqual(food.index, -69.04318181818182)
        self.assertEqual(food.name, "Frostings, glaze, prepared-from-recipe")

# class ТestDatabase(unittest.TestCase):

#     def test_write(self):
#         db.save_log(12,14555)

#         self.assertEqual(food.index, -69.04318181818182)

#     def test_encrypt(self):
#         pass


unittest.main()
