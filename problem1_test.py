import unittest
from problem1 import Solution
from problem1_optimized import Solution as Optimized

class TestSolution(unittest.TestCase):
    solution = Solution()
    optimized_solution = Optimized()

    def test1(self):
        self.assertEqual(self.solution.twoSum([2,7,11,15], 9), [0,1])

    def test2(self):
        self.assertEqual(self.solution.twoSum([3,2,4], 6), [1,2])

    def test3(self):
        self.assertEqual(self.solution.twoSum([3,3], 6), [0,1])

    def test1(self):
        self.assertEqual(self.optimized_solution.twoSum([2,7,11,15], 9), [0,1])

    def test2(self):
        self.assertEqual(self.optimized_solution.twoSum([3,2,4], 6), [1,2])

    def test3(self):
        self.assertEqual(self.optimized_solution.twoSum([3,3], 6), [0,1])

if __name__ == '__main__':
    unittest.main()
