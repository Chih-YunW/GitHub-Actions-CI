import unittest
import example


class TestCase(unittest.TestCase):
    def test_add_l(self):
        self.assertEqual(example.add(1, 2), 3)

    def test_sub_l(self):
        self.assertEqual(example.sub(1, 1), 0)

    def test_mul_l(self):
        self.assertEqual(example.mul(1, 2), 2)

    def test_div_l(self):
        self.assertEqual(example.div(5, 1), 5)


if __name__ == '__main__':
    unittest.main()
