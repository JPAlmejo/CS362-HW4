import unittest
import cubeVolume

class TestCaseCubeVolume(unittest.TestCase):
#tests basic inputs
    def test1(self):
        self.assertEqual(cubeVolume.volume(1, 2, 3), 6)

#another test of basic inputs
    def test2(self):
        self.assertEqual(cubeVolume.volume(5, 5, 5), 125)

#=========================================================
#testing negative inputs (fail)
    def test3(self):
        self.assertEqual(cubeVolume.volume(-5, 5, 5), 125)

#testing decimal float points (failed)
    def test4(self):
        self.assertEqual(cubeVolume.volume(5.5, 3.25, 2), 35.64)

#testing some strings (fail & error)
    def test5(self):
        self.assertEqual(cubeVolume.volume(three, two, one), six)

if __name__== '__main__':
    unittest.main(verbosity=2)