"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        fast, slow = head, head

        while fast.next:
            if not fast.next.next:
                return False
            fast = fast.next.next 
            slow = slow.next
            if fast is slow:
                return True
        return False
    
"""
Floyd's cycle-finding algorithm 'Tortoise and hare'

The idia is such that start a tortoise running on a loop with a speed of 1 and start a hare with a speed of 2, then, in time, they will meet at the same spot before the hare does the full cycle. Why is that? Let's imagine that the length of the cycle is N. Once they start running the distance between them  is N. After the first iteration hare is up by 2 while tortoise is up by only 1. So at first tortoise increased the distance between them by 1 but the hare shortened it by 2. Therefore the overall distance needed for the hare to go is (N+1-2) which is just N-1.

So we know for sure that:
    1. They will meet at the same place eventually
    2. The will meet at least in N steps. 

Time complexity is O(n). Since we might have to  traverse the whole linked list.
Space complexity is constant O(1). Since we only need to store two pointers to the 'hare' and the 'tortoise'
"""
