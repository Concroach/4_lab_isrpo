import unittest


class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3), 9)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(7), 2) # FAIL
        self.assertEqual(area(0.123), 1) # FAIL


    def test_perimeter(self):
        self.assertEqual(perimeter(3), 12)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(9), 14) # FAIL
        self.assertEqual(perimeter('string'), 14) # FAIL


def area(a):
    """
    Вычисляет значение площади квадрата.

    Принимает параметр a (int) - сторона квадрата.
    
    Возвращает int значение площади квадрата.
    """
    return a * a


def perimeter(a):
    """
    Вычисляет значение периметра квадрата.

    Принимает параметр a (int) - сторона квадрата.
    
    Возвращает int значение периметра квадрата.
    """
    return 4 * a