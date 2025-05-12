import unittest
from src.service.items import dummy_method_test

class ItemsTest(unittest.TestCase):

    def test_sample(self):
        result = dummy_method_test()
        self.assertEqual("expected", result)

if __name__ == '__main__':
    unittest.main()
