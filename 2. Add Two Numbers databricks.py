# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def helper(head):
            s = ""
            temp = head

            while temp:
                s += str(temp.val)
                temp = temp.next

            return int(s[::-1])

        num1 = helper(l1)
        num2 = helper(l2)

        newVal = str(num1 + num2)[::-1]

        head = ListNode(int(newVal[0]))
        temp = head
        m = len(newVal)

        for j in range(1, m):
            node = ListNode(int(newVal[j]))
            temp.next = node
            temp = temp.next

        return head
