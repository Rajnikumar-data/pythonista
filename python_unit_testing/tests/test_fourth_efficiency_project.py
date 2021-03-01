import time
import unittest
from fourth_efficiency_project import FibonacciSequence


class TestEfficiency(unittest.TestCase):

    def setUp(self):
        self._fibonacci_sequence = FibonacciSequence()
        self._efficiency_data = dict()

    def test_first_method(self):
        start_time = time.time()
        self._fibonacci_sequence.recursive_method(30)
        end_time = time.time()
        self._efficiency_data['recursive_method'] = (end_time - start_time)

    def test_second_method(self):
        start_time = time.time()
        self._fibonacci_sequence.math_method(30)
        end_time = time.time()
        self._efficiency_data['math_method'] = (end_time - start_time)
       
    def tearDown(self):
        print(self._efficiency_data)
        self._fibonacci_sequence = None
        self._efficiency_data.clear()


if __name__ == '__main__':
    unittest.main()

