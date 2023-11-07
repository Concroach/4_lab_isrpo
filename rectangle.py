import unittest


class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3, 4), 12)
        self.assertEqual(area(0, 9), 0)
        self.assertEqual(area(1, 9), 0) # FAIL
        self.assertEqual(area(1), 0) # FAIL



    def test_perimeter(self):
        self.assertEqual(perimeter(5, 5), 20)
        self.assertEqual(perimeter(1, 9), 20)
        self.assertEqual(perimeter(0, 9), 123456) # FAIL
        self.assertEqual(perimeter(1, 'string'), 7) # FAIL



def area(a, b):
    """
    Вычисляет значение площади прямоугольника.
    
    Принимает 2 параметра:
      Параметр a (int) - первая сторона прямоугольника.
      Параметр b (int) - вторая сторона прямоугольника.

    Возвращает int значение площади прямоугольника.
    """
    return a * b 


def perimeter(a, b): 
    """
    Вычисляет значение периметра прямоугольника.
    Принимает 2 параметра:
      Параметр a (int) - первая сторона прямоугольника.
      Параметр b (int) - вторая сторона прямоугольника.

    Возвращает int значение периметра прямоугольника.
    """
    return (a + b) * 2