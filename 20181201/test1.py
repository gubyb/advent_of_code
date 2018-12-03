import unittest
import chronal_calibration_1, chronal_calibration_2

class Test_TestGivenExamples_1(unittest.TestCase):
    def test_1(self):
        lines = ['+1', '+1', '+1']
        self.assertEqual(chronal_calibration_1.chronal_calibration(lines), 3)

    def test_2(self):
        lines = ['+1', '+1', '-2']
        self.assertEqual(chronal_calibration_1.chronal_calibration(lines), 0)

    def test_3(self):
        lines = ['-1', '-2', '-3']
        self.assertEqual(chronal_calibration_1.chronal_calibration(lines), -6)

class Test_TestGivenExamples_2(unittest.TestCase):
    def test_1(self):
        lines = ['+1', '-1']
        self.assertEqual(chronal_calibration_2.chronal_calibration(lines), 0)

    def test_2(self):
        lines = ['+3', '+3', '+4', '-2', '-4']
        self.assertEqual(chronal_calibration_2.chronal_calibration(lines), 10)

    def test_3(self):
        lines = ['-6', '+3', '+8', '+5', '-6']
        self.assertEqual(chronal_calibration_2.chronal_calibration(lines), 5)

    def test_4(self):
        lines = ['+7', '+7', '-2', '-7', '-4']
        self.assertEqual(chronal_calibration_2.chronal_calibration(lines), 14)

if __name__ == '__main__':
    unittest.main()