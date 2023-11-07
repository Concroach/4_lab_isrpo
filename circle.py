import math
import unittest


class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3), 28.274333882308138)
        self.assertEqual(area(5), 78.53981633974483)
        self.assertEqual(area(10), 314) # FAIL
        self.assertEqual(area('string'), 54) # FAIL




    def test_perimeter(self):
        self.assertEqual(perimeter(3), 18.84955592153876)
        self.assertEqual(perimeter(5), 31.41592653589793)
        self.assertEqual(perimeter(10), 62) # FAIL
        self.assertEqual(area('string'), 'fail') # FAIL




def area(r):
    """
    Вычисляет площадь круга по формуле.

    Принимает параметр r (int) - радиус круга для вычисления площади.

    Возвращает int значение площади круга.
     """
    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет периметр круга по формуле.

    Принимает параметр r (int) - радиус круга для вычисления периметра.

    Возвращает int значение периметра круга.
    """
    return 2 * math.pi * r