import unittest
import listAverage

class TestCaseListAverage(unittest.TestCase):
#tests basic inputs
    def test1(self):
        self.assertEqual(listAverage.listAverage([3, 3, 3]),3)

#tests basic inputs again
    def test2(self):
        self.assertEqual(listAverage.listAverage([2, 5, 10, 20]),9.25)

#======================================================================

#tests negative inputs (pass)
    def test3(self):
        self.assertEqual(listAverage.listAverage([-3, -25, -4]), −10.66666667)

#tests decimal floating numbers (pass)
    def test4(self):
        self.assertEqual(listAverage.listAverage([2.5, 2.3, 5.8, 9]),4.9)

#tests combination of a bunch of different kind of numbers (fail) floating number is almost infinite.
    def test5(self):
        self.assertEqual(listAverage.listAverage([-4, 2.5, 0, 45, -3, 222, 45]),43.93)

#tests an empty list that has only a zero (pass)
    def test6(self):
        self.assertEqual(listAverage.listAverage([0]),0)

if __name__== '__main__':
    unittest.main(verbosity=2)