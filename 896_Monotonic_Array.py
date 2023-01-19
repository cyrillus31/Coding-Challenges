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