import unittest

class SquareTestCase(unittest.TestCase):
    def test_zelo_mul1(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_mul2(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_square_mul3(self):
        res = area(15)
        self.assertEqual(res, 225)

    def test_square_mul4(self):
        res = area(1.2)
        self.assertEqual(res, 1.44)

    def test_square_mul5(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_square_mul6(self):
        res = perimeter(1.2)
        self.assertEqual(res, 4.8)

    def test_square_mul7(self):
        res = perimeter(100)
        self.assertEqual(res, 400)