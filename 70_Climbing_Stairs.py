# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Checkout NeetCode's YouTube video (dynamic programming):
# https://youtu.be/Y0lT9Fck7qI
# Also checkout wikipedia on Dynamic Programming https://en.wikipedia.org/wiki/Dynamic_programming


class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 1
        for element in range(n-1):
            temp = first
            first = first + second
            second = temp
        return first
    
mySolution = Solution()
print(mySolution.climbStairs(4))





            









