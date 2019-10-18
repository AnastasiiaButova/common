import unittest

from tests.homework import (Rectangle)

class MyTestCase(unittest.TestCase):

    def test_init(self):
        rectangle = Rectangle(3,4)
        self.assertTrue(True)

    def test_rectangle_perimeter(self):
        rectangle = Rectangle(3,4)
        self.assertEqual(Rectangle.get_rectangle_perimeter(rectangle), 14)


    def test_rectangle_square(self):
        rectangle = Rectangle(3,4)
        self.assertEqual(Rectangle.get_rectangle_square(rectangle), 12)


    def test_sum_of_corners_true(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(Rectangle.get_sum_of_corners(rectangle, 1), 90)
        self.assertEqual(Rectangle.get_sum_of_corners(rectangle, 2), 180)
        self.assertEqual(Rectangle.get_sum_of_corners(rectangle, 3), 270)
        self.assertEqual(Rectangle.get_sum_of_corners(rectangle, 4), 360)

    def test_sum_of_corners_false(self):
        rectangle = Rectangle(3,4)
        with self.assertRaises(ValueError):
            Rectangle.get_sum_of_corners(rectangle, 5)


    def test_rectangle_diagonal(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(Rectangle.get_rectangle_diagonal(rectangle), 5)


    def test_radius_of_circumscribed_circle(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(Rectangle.get_radius_of_circumscribed_circle(rectangle), 2.5)


    def test_radius_of_inscribed_circle(self):
        rectangle = Rectangle(14, 14)
        self.assertEqual(Rectangle.get_radius_of_inscribed_circle(rectangle), 7)

    def test_radius_of_inscribed_circle_false(self):
        rectangle = Rectangle(4,3)
        with self.assertRaises(ValueError):
            Rectangle.get_radius_of_inscribed_circle(rectangle)


if __name__ == '__main__':
    unittest.main()
