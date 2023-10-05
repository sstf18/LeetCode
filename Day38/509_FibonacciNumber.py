# dp array : dp[i] the i-th fibonacci number
# formula : dp[n] = dp[n - 1] + dp[n - 2]
# dp init : dp[0] = 0; dp[1] = 1
# train sequnce: from front to end 
# print 

class Solution:
    def fib(self, n: int) -> int:
        if n == 0: 
            return 0 

        dp = [0] * (n + 1)

        dp[0] = 0 
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i -2]
        return dp[n]


import unittest

class TestSolution(unittest.TestCase):
    def test_fib(self):
        solution = Solution()

        self.assertEqual(solution.fib(0), 0)
        self.assertEqual(solution.fib(1), 1)
        self.assertEqual(solution.fib(2), 1)
        self.assertEqual(solution.fib(3), 2)
        self.assertEqual(solution.fib(4), 3)
        self.assertEqual(solution.fib(5), 5)
        self.assertEqual(solution.fib(6), 8)
        self.assertEqual(solution.fib(7), 13)
        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
#using the 5 steps to solve dp problem. 