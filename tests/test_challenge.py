import unittest
from challenge import counter

class EasyTestCase(unittest.TestCase):
    def test_easy_input(self):
        self.assertEquals(counter("rajni"), 5)

    def test_easy_input_two(self):
        self.assertEquals(counter("MO"), 2)

class MediumTestCase(unittest.TestCase):
    def test_medium_input(self):
        with self.assertRaises(ValueError):
            self.assertEquals(counter("M%$#98"), 6)

    def test_medium_input_two(self):
        with self.assertRaises(ValueError):
            self.assertEquals(counter("raj  ni"), 7)

class HardTestCase(unittest.TestCase):
    def test_hard_input(self):
        with self.assertRaises(ValueError):
            self.assertEquals(counter(""), 0)

    def test_hard_input_two(self):
        with self.assertRaises(ValueError):
            self.assertEquals(counter(None), 4)




if __name__ == '__main__':
    unittest.main()
