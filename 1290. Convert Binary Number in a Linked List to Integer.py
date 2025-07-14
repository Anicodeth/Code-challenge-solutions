# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        k = 0
        temp = head

        while temp:
            k += 1
            temp = temp.next

        temp = head
        value = 0
        for i in range(k - 1, -1, -1):
            if temp.val:
                value += (2 ** i) 
            temp = temp.next

        return value

        
