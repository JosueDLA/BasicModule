import unittest
from jdla_basic import basic_operations


class Test_basic_opea(unittest.TestCase):

    def test_add(self):
        self.assertEqual(basic_operations.addition(10, 5), 15)
        self.assertEqual(basic_operations.addition(-1, 1), 0)
        self.assertEqual(basic_operations.addition(1, -1), 0)
        self.assertEqual(basic_operations.addition(-1, -1), -2)

    def test_sub(self):
        self.assertEqual(basic_operations.substraction(10, 5), 5)
        self.assertEqual(basic_operations.substraction(-1, 1), -2)
        self.assertEqual(basic_operations.substraction(1, -1), 2)
        self.assertEqual(basic_operations.substraction(-1, -1), -0)

    def test_multi(self):
        self.assertEqual(basic_operations.multiplication(10, 5), 50)
        self.assertEqual(basic_operations.multiplication(-1, 1), -1)
        self.assertEqual(basic_operations.multiplication(1, -1), -1)
        self.assertEqual(basic_operations.multiplication(-1, -1), 1)

    def test_divi(self):
        self.assertEqual(basic_operations.division(10, 5), 2)
        self.assertEqual(basic_operations.division(-1, 1), -1)
        self.assertEqual(basic_operations.division(1, -1), -1)
        self.assertEqual(basic_operations.division(-1, -1), 1)

        # self.assertRaises Value expected, method, args
        self.assertRaises(ValueError, basic_operations.division, 10, 0)

        # Test Exception using context manager
        with self.assertRaises(ValueError):
            basic_operations.division(10, 0)


if __name__ == '__main__':
    unittest.main()
