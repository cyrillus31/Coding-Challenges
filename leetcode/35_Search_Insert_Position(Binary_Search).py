class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else: 
                right = mid
        if nums[mid] > target:
            return mid
        else:
            return mid + 1 

my_solution = Solution()
a = my_solution.searchInsert([1,2,3,5,6], 10)
print("\nIndex is {}".format(a))

