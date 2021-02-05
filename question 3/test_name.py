import unittest
import name

class TestCaseName(unittest.TestCase):
#tests basic inputs
    def test1(self):
        self.assertEqual(name.name("john", "perez"),"john perez")

#===============================================================

#tests string numbers inputs (error and fail)
    def test2(self):
        self.assertEqual(name.name("two", "one"),"two one")

#tests numbers as inputs (pass)
    def test3(self):
        self.assertEqual(name.name("1", "2"), "1 2")

#tests first or last names that have different parts (pass)
    def test4(self):
        self.assertEqual(name.name("John Jesus", "Perez Almejo De La Cruz"), "John Jesus Perez Almejo De La Cruz")

if __name__== '__main__':
    unittest.main(verbosity=2)