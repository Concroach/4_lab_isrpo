# Документация тестов. 4 Лабораторная работа ИСРПО

## Цели и задачи тестирования
- Проверить правильность расчета площади и периметра фигур.
- Убедиться, что функции корректно обрабатывают входные данные и возвращают ожидаемый Ожидаемый Результат.
- Выявить и исправить любые ошибки или несоответствия в функциях.
    Для выполнения работы необходимо написать тесты, написать докуменатацию в readme.md, составить метрики, написать отчёт.

## Описание тестируемого продукта
Продукт представляет из себя четыре py файла: circle.py, rectangle.py, triangle.py, square.py, которые содержат в себе функции вычисления площади и периметра четырех фигур: круга, прямоугольника, треугольника, квадрата, соответсветнно.
Требуется протестировть корректность ответов данных функций.

## Область тестирования
#### circle.py
Тестирование функции **area** с помощью метода test_area.
Тестирование функции **perimeter** с помощью метода test_perimeter.
#### rectangle.py
Тестирование функции **area**  с помощью метода test_area.
Тестирование функции **perimeter** с помощью метода test_perimeter.
#### square.py
Тестирование функции **area**  с помощью метода test_area.
Тестирование функции **perimeter** с помощью метода test_perimeter.
#### rectangle.py
Тестирование функции **area**  с помощью метода test_area.
Тестирование функции **perimeter** с помощью метода test_perimeter.

## Стратегия тестирования
Функциональное тестирование: 
- Для каждого файла создаем класс *FileName*TestCase, в котором прописываем 2 теста test_area и test_perimiter.
- Метод test_area, проверяет правильность вычисления площади фигуры для разных значений. Для каждого значения используется утверждение self.assertEqual, которое сравнивает ожидаемый Ожидаемый Результат с фактическим результатом выполнения функции area. Аргументы в метод self.assertEqual включают ожидаемый Ожидаемый Результат и фактический Ожидаемый Результат. Если результаты не совпадают, тест считается неудачным.
- Метод test_perimiter, проверяет правильность вычисления периметра фигуры для разных значений. Для каждого значения используется утверждение self.assertEqual, которое сравнивает ожидаемый Ожидаемый Результат с фактическим результатом выполнения функции perimiter. Аргументы в метод self.assertEqual включают ожидаемый Ожидаемый Результат и фактический Ожидаемый Результат. Если результаты не совпадают, тест считается неудачным.

## Критерии приемки
Для успешного завершения тестирования и приемки продукта необходимо:
- Все тесты успешно выполнены.
- Результаты тестирования соответствуют ожидаемым значениям.
- Найденные ошибки или несоответствия устранены.

## Ожидаемые результаты
Ожидается получение отчетов о выполненных тестах, общих результатов тестирования.

### CircleTestCase
```python
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
```

| Название теста | Ввод | Ожидаемый Результат | Прошел тест или нет |
|----------------|------|---------------------|---------------------|
| test_area      | 3    | 28.274333882308138  | <span style="color:green">true</span> |
| test_area      | 5    | 78.53981633974483   | <span style="color:green">true</span> |
| test_area      | 10   | 312                 | <span style="color:red">false</span> |
| test_area      | 'string' | 54              | <span style="color:red">false</span> |
| test_perimeter | 3    | 18.84955592153876   | <span style="color:green">true</span> |
| test_perimeter | 5    | 31.41592653589793   | <span style="color:green">true</span> |
| test_perimeter | 10   | 62                  | <span style="color:red">false</span> |
| test_perimeter | 'string' | 'fail'          | <span style="color:red">false</span> |

### RectangleTestCase 
```python
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
```

| Название теста | Ввод | Ожидаемый Результат | Прошел тест или нет |
|----------------|------|---------------------|---------------------|
| test_area     | (3, 4)  | 12   | <span style="color:green">true</span> |
| test_area     | (0, 9)  | 0    | <span style="color:green">true</span> |
| test_area     | (1, 9)  | 0    | <span style="color:red">false</span> |
| test_area     | (1)     | 0    | <span style="color:red">false</span> |
| test_perimeter| (5, 5)  | 20   | <span style="color:green">true</span> |
| test_perimeter| (1, 9)  | 20   | <span style="color:green">true</span> |
| test_perimeter| (0, 9)  | 123456 | <span style="color:red">false</span> |
| test_perimeter| (1, 'string') | 'fail' | <span style="color:red">false</span> |

### TriangleTestCase 
```python
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
```

| Название теста | Ввод | Ожидаемый Результат | Прошел тест или нет |
|----------------|------|-----------|---------------------|
| test_area     | (3, 4)  | 6    | <span style="color:green">true</span> |
| test_area     | (5, 7)  | 17.5 | <span style="color:green">true</span> |
| test_area     | (10, 9)  | 2332 | <span style="color:red">false</span> |
| test_area     | (2, 1, 8) | 90   | <span style="color:red">false</span> |
| test_perimeter| (3, 4, 5)  | 12   | <span style="color:green">true</span> |
| test_perimeter| (10.5, 6, 8)  | 24.5   | <span style="color:green">true</span> |
| test_perimeter| (2, 1, 8)  | 90   | <span style="color:red">false</span> |
| test_perimeter| ('string', 8) | 'fail'   | <span style="color:red">false</span> |

### SquareTestCase
```python
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
```
| Название теста | Ввод | Результат | Прошел тест или нет |
|----------------|------|-----------|---------------------|
| test_area     | (3, 9)  | 13.5 | <span style="color:green">true</span> |
| test_area     | (0, 0)  | 0    | <span style="color:green">true</span> |
| test_area     | (7, 2)  | 14   | <span style="color:red">false</span> |
| test_area     | (0.123) | 'fail' | <span style="color:red">false</span> |
| test_perimeter| (3, 12)  | 30   | <span style="color:green">true</span> |
| test_perimeter| (0, 0)   | 0    | <span style="color:green">true</span> |
| test_perimeter| (9, 14)  | 46   | <span style="color:red">false</span> |
| test_perimeter| ('string', 14) | 'fail'   | <span style="color:red">false</span> |

### Общие метрики
| Всего тестов | Выполнено | Провалено |
|--------------|-----------|-----------|
| 32           | <span style="color:green">16</span> | <span style="color:red">16</span> |
