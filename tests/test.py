import unittest

from tests.homework import (Rectangle)

class MyTestCase(unittest.TestCase):

    def test_init(self):
        rectangle = Rectangle(3,4)
        self.assertTrue(True)

    def test_rectangle_perimeter(self, width, height):
        perimeter = Rectangle(3,4)
        self.assertEqual(Rectangle.get_rectangle_perimeter(perimeter), 14)


    def test_rectangle_square(self):
        square = Rectangle(3,4)
        self.assertEqual(Rectangle.get_rectangle_square(square), 12)


    def test_sum_of_corners_true(self):
        sum_of_corners = Rectangle(3, 4)
        self.assertEqual(Rectangle.get_sum_of_corners(sum_of_corners, 1), 90)
        self.assertEqual(Rectangle.get_sum_of_corners(sum_of_corners, 2), 180)
        self.assertEqual(Rectangle.get_sum_of_corners(sum_of_corners, 3), 270)
        self.assertEqual(Rectangle.get_sum_of_corners(sum_of_corners, 4), 360)

    def test_sum_of_corners_false(self):
        sum_of_corners = Rectangle(3,4)
        with self.assertRaises(ValueError):
            Rectangle.get_sum_of_corners(sum_of_corners, 5)


    def test_rectangle_diagonal(self):
        diagonal = Rectangle(3, 4)
        self.assertEqual(Rectangle.get_rectangle_diagonal(diagonal), 5)


    def test_radius_of_circumscribed_circle(self):
        radius = Rectangle(3, 4)
        self.assertEqual(Rectangle.get_radius_of_circumscribed_circle(radius), 2.5)


    def test_radius_of_inscribed_circle(self):
        radius = Rectangle(14, 14)
        self.assertEqual(Rectangle.get_radius_of_inscribed_circle(radius), 7)

    def test_radius_of_inscribed_circle_false(self):
        radius = Rectangle(4,3)
        with self.assertRaises(ValueError):
            Rectangle.get_radius_of_inscribed_circle(radius)


if __name__ == '__main__':
    unittest.main()
