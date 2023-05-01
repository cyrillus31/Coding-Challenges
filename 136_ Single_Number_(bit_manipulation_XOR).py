"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
______________________

The OR operator is represented by the symbol |. It returns a 1 in each bit position for which the corresponding bits of either one or both operands are 1s. Otherwise, it returns a 0.

Here’s an example:
5 = 101
3 = 011
5 | 3 = 111

The XOR operator is represented by the symbol ^. It returns a 1 in each bit position for which the corresponding bits of either but not both operands are 1s. Otherwise, it returns a 0.
Here’s an example:
5 = 101
3 = 011
5 ^ 3 = 110
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n
        return result        
