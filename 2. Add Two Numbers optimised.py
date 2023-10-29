# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        carry = 0
        while l1 or l2 or carry:
            val1  = l1.val if l1 else 0
            val2  = l2.val if l2 else 0

            sumi = val1 + val2 + carry
            carry = sumi // 10
            red = sumi % 10

            if head:
                temp.next = ListNode(red)
                temp = temp.next
            else:
                head = ListNode(red)
                temp = head

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return head
