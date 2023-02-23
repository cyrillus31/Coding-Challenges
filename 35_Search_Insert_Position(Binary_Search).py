# iterative binary search

def binarySearch(nums, target):
    low = 0
    high = len(nums)-1

    while len(nums[low:high+1]) > 1:
        mid = (low + high) // 2

        if target > nums[mid]:
            print("Checking %s while mid is %s" % (nums[low:high+1], nums[mid]))
            low = mid + 1

        elif target < nums[mid]:
            print("Checking %s while mid is %s" % (nums[low:high+1], nums[mid]))
            high = mid
        
        else:
            print("Checking %s while mid is %s" % (nums[low:high+1], nums[mid]))
            return mid
        
    mid = (low + high) // 2
    if target > nums[mid]:
        print("Checkinggg %s while mid is %s" % (nums[low:high+1], nums[mid]))
        return mid + 1
    else: 
        print("Checkinggg %s while mid is %s" % (nums[low:high+1], nums[mid]))
        return mid

        

a = binarySearch([1,2,3,5,6], 7)
print("\nIndex is {}".format(a))

