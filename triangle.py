import unittest


class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3, 4), 6)
        self.assertEqual(area(5, 7), 17.5)
        self.assertEqual(area(10, 9), 2332) # FAIL
        self.assertEqual(area(2, 1, 8), 90) # FAIL



    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(10.5, 6, 8), 24.5)
        self.assertEqual(perimeter(2, 1, 8), 90) # FAIL
        self.assertEqual(perimeter('string', 8), 20) # FAIL




def area(a, h):
    """
    Вычисляет Значение площади треугольника.
    Принимает 2 параметра:
      Параметр a (int) - сторона треугольника.
      Параметр h (int) - высота треугольника к стороне a.
    Возвравщает int значение площади треугольника.
    """
    return a * h / 2

def perimeter(a, b, c):
    """
    Вычисляет значение периметра треугольника.
    Принимает 3 параметра:
      Параметр a (int) - 1 сторона треугольника.
      Параметр b (int) - 2 сторона треугольника.
      Параметр c (int) - 3 сторона треугольника.
    Возвравщает int значение периметра.
    """
    return a + b + c