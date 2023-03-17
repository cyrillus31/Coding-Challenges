class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        c = 0
        l = len(nums)

        if l == 1:
            return 1
        
        for index in range(1, l):
            left = nums[c]
            right = nums[index]

            if left != right:
                nums[c+1] = nums[index]
                c += 1
        
        return c+1, nums

mySolution = Solution()
nums = [1,1,2]
print(mySolution.removeDuplicates(nums))
