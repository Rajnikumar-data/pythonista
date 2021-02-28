import unittest
from second_project import Counter

# setUp for instantiate object to access the class so
# that object need not to be accessed again and again
# teardown for instantiate object to none
class EasyTestCase(unittest.TestCase):

    def setUp(self):
        self.counter = Counter()

    def test_easy_input(self):
        self.assertEqual(self.counter.get_value(),0)

    def test_easy_input_two(self):
        self.counter.clear()
        self.assertEqual(self.counter.get_value(),0)

    def teardown(self):
        self.counter = None