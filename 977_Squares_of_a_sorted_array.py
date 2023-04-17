"""Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        d = []
        for number in nums:
            sq = number ** 2
            d.append(sq)
        return sorted(d)
