import math


def square_area(side):
    """Returns the area of a square"""
    return side * side


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    return base * height


def triangle_area(base, height):
    """Returns the area of a triangle"""
    return (base * height) / 2


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    return (diagonal_1 * diagonal_2) / 2


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    return (base_major * base_minor * height) / 2


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    return (perimeter * apothem) / 2


def circumference_area(radius):
    """Returns the area of a circumference"""
    return round(math.pi * radius**2, 2)


if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):
        def setUp(self):
            # Initialize the needed values for the tests
            self.square = {4: 2, 16: 4, 25: 5}
            self.rectangle = {12: [3, 4], 48: [6, 8], 56: [7, 8]}
            self.triangle = {6: [3, 4], 24: [6, 8], 28: [7, 8]}
            self.rhombus = {8: [4, 4], 18: [6, 6], 6: [4, 3]}
            self.trapezoid = {12: [3, 4, 2], 15: [3, 5, 2], 84: [7, 8, 3]}
            self.polygon = {6: [3, 4], 24: [6, 8], 28: [7, 8]}
            self.circumference = {50.27: 4, 201.06: 8, 78.54: 5}

        def test_square_area(self):
            for key, value in self.square.items():
                self.assertEqual(key, square_area(value))

        def test_rectangle_area(self):
            for key, values in self.rectangle.items():
                self.assertEqual(key, rectangle_area(values[0], values[1]))

        def test_triangle_area(self):
            for key, values in self.triangle.items():
                self.assertEqual(key, triangle_area(values[0], values[1]))

        def test_rhombus_area(self):
            for key, values in self.rhombus.items():
                self.assertEqual(key, rhombus_area(values[0], values[1]))

        def test_trapezoid_area(self):
            for key, values in self.trapezoid.items():
                self.assertEqual(key, trapezoid_area(values[0], values[1], values[2]))

        def test_regular_polygon_area(self):
            for key, values in self.polygon.items():
                self.assertEqual(key, regular_polygon_area(values[0], values[1]))

        def test_circumference_area(self):
            for key, value in self.circumference.items():
                self.assertEqual(key, circumference_area(value))

        def tearDown(self):
            # Delete the needed values for the tests
            del(self.square)
            del(self.rectangle)
            del(self.triangle)
            del(self.rhombus)
            del(self.trapezoid)
            del(self.polygon)
            del(self.circumference)

    unittest.main()
