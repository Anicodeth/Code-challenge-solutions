# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def traverse(root):
            num = []
            temp = root

            while temp:
                num.append(str(temp.val))
                temp = temp.next

            return int("".join(num[::-1]))

        first = traverse(l1)
        second = traverse(l2)

        sumVal = str(first + second)[::-1] 

        head = ListNode(int(sumVal[0]))
        temp = head

        for i in range(1, len(sumVal)):
            node = ListNode(int(sumVal[i]))
            temp.next = node
            temp = temp.next

        return head

