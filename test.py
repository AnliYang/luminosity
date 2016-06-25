import luminosity
import os
import unittest

class TestLuminosity(unittest.TestCase):

    def setUp(self):
        self.fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures')

    def test_white(self):
        path = os.path.join(self.fixtures_path, 'white.png')
        self.assertEqual(luminosity.get_brightness(path), 255.0)

        path = os.path.join(self.fixtures_path, 'white_with_transparency.png')
        self.assertEqual(luminosity.get_brightness(path), 255.0)

    def test_black(self):
        path = os.path.join(self.fixtures_path, 'black.png')
        self.assertEqual(luminosity.get_brightness(path), 0.0)

        path = os.path.join(self.fixtures_path, 'black_with_transparency.png')
        self.assertEqual(luminosity.get_brightness(path), 0.0)

    def test_transparent(self):
        path = os.path.join(self.fixtures_path, 'transparent.png')
        self.assertEqual(luminosity.get_brightness(path), 0.0)

    def test_red(self):
        path = os.path.join(self.fixtures_path, 'red.png')
        self.assertEqual(luminosity.get_brightness(path), 54.213)

        path = os.path.join(self.fixtures_path, 'red_with_transparency.png')
        self.assertEqual(luminosity.get_brightness(path), 54.213)

    def test_green(self):
        path = os.path.join(self.fixtures_path, 'green.png')
        self.assertEqual(luminosity.get_brightness(path), 182.376)

        path = os.path.join(self.fixtures_path, 'green_with_transparency.png')
        self.assertEqual(luminosity.get_brightness(path), 182.376)

    def test_blue(self):
        path = os.path.join(self.fixtures_path, 'blue.png')
        self.assertEqual(luminosity.get_brightness(path), 18.411)

        path = os.path.join(self.fixtures_path, 'blue_with_transparency.png')
        self.assertEqual(luminosity.get_brightness(path), 18.411)

    def test_unreadable(self):
        path = os.path.join(self.fixtures_path, 'nonsense.png')
        with self.assertRaises(IOError):
            luminosity.get_brightness(path)

    def test_not_image(self):
        path = __file__
        with self.assertRaises(IOError):
            luminosity.get_brightness(path)

    def test_gif(self):
        path = os.path.join(self.fixtures_path, 'aguilera.gif')
        self.assertEqual(luminosity.get_brightness(path), 43.562)

    def test_no_path(self):
        path = None
        with self.assertRaises(TypeError) as cm:
            luminosity.get_brightness(path)
        self.assertEqual(cm.exception.message, "File path must be provided.")

    def test_get_brightest(self):
        path1 = os.path.join(self.fixtures_path, 'white.png')
        path2 = os.path.join(self.fixtures_path, 'black.png')
        self.assertEqual(luminosity.get_brightest([path1, path2]), (255.0, path1))

    def test_get_brightest_duds(self):
        path1 = os.path.join(self.fixtures_path, 'white.png')
        path2 = os.path.join(self.fixtures_path, 'nonsense.png')
        self.assertEqual(luminosity.get_brightest([path1, path2]), (255.0, path1))

if __name__ == '__main__':
    unittest.main()
