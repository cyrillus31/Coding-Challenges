"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array."""

def moveZeroes(nums: list[int]) -> None:
    # feels like bubble sort
    l = len(nums)
    if l < 2:
        return
    left = 0
    right = 1
    while right <= l-1:
        if nums[left] == 0 and nums[right] != 0: 
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right + 1
            continue
        if nums[left] == 0 and nums[right] == 0:
            right += 1
            continue
        left, right = left + 1, right + 1

arr = [0,2,45,0,342,0,34,0,0]

moveZeroes(arr)



