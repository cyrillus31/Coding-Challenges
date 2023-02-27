"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i1 in range(len(nums)):
            for i2 in range(i1+1, len(nums)):
                if nums[i1]+nums[i2] == target:
                    return [i1, i2]
                else:
                    continue

