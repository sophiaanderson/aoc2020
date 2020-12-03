import unittest
import puzzle
import puzzle2

class TestBasic(unittest.TestCase):
    def test_pass(self):
        data = puzzle2.parse(file("input.txt").readlines())
        answer = puzzle2.solve(data)
        self.assertNotEqual(0, answer)

if __name__ == '__main__':
    unittest.main()
