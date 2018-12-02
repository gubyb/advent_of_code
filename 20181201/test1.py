import unittest
import chronal_calibration

class Test_TestGivenExamples(unittest.TestCase):
    def test_1(self):
        lines = ['+1', '+1', '+1']
        self.assertEqual(chronal_calibration.chronal_calibration(lines), 3)

    def test_2(self):
        lines = ['+1', '+1', '-2']
        self.assertEqual(chronal_calibration.chronal_calibration(lines), 0)

    def test_3(self):
        lines = ['-1', '-2', '-3']
        self.assertEqual(chronal_calibration.chronal_calibration(lines), -6)

if __name__ == '__main__':
    unittest.main()