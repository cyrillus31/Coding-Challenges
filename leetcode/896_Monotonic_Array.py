# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. 
# An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# Given an integer array nums, return true if the given array is monotonic, 
# or false otherwise.

class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
            decreasing = False
            increasing = False
            
            for n in range(len(nums)-1):
                if nums[n] == nums[n+1]:
                    pass
                elif nums[n] < nums[n+1] and decreasing == False:
                    increasing = True
                elif nums[n] > nums[n+1] and increasing == False:
                    decreasing = True 
                else:
                    return False
            return True

nums = [2,2,2,1,4,5]
my = Solution()
print(my.isMonotonic(nums))