"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]


Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

class ListNode:
    """A class to create nodes of a linked list"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# The following is a way to create linked lists by hand
    # ln1 = ListNode(2, ListNode(4, ListNode(3, next=None)))
    # ln2 = ListNode(5, ListNode(6, ListNode(4, next=None)))

def constructListNode(values: list[int], index=0):
    """This allows you to construct instances of ListNode class based on a list of inputs"""
    while index <= len(values)-1:
        return ListNode(values[index], constructListNode(values, index + 1))

ln1 = constructListNode([2,4,3])
ln2 = constructListNode([5,6,4])

def unpack(ListNode, thevalues):
    """This allows you to unpack a linked list into Python's list"""
    thevalues.append(ListNode.val)
    if ListNode.next != None:
        nextThing = ListNode.next
        return unpack(ListNode.next, thevalues)
    else:
        return thevalues 

def addTwoNumbers(l1, l2):
    
    number1 = sum([digit*(10**index) for index, digit in enumerate(unpack(l1, []))])
    number2 = sum([digit*(10**index) for index, digit in enumerate(unpack(l2, []))])
    theSum = number1 + number2
    print(number1, number2, theSum)
    
    return constructListNode([int(digit) for digit in str(theSum)[::-1]])

result = addTwoNumbers(ln1, ln2)
print(result)
print(unpack(result, []))