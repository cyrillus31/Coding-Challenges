"""
Given an array arr of positive integers sorted in a strictly increasing order, 
and an integer k.
Return the kth positive integer that is missing from this array.

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length
"""

class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        rcounter = 0
        counter = 0
        element = 1
        while True:
            if arr == []:
                return 0 

            try:
                if element == arr[counter]:
                    counter += 1
                    continue

                else:
                    rcounter += 1

            except:
                rcounter += 1

            finally:
                if rcounter == k:
                    return element
                else:
                    element += 1

mySolution = Solution()
print(mySolution.findKthPositive([2,3,4,7,11], 3))
        

