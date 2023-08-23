# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      arr = []

      while head:
        arr.append(head.val)
        head = head.next
      
      arr.sort()
      head = temp = None
      for num in arr:
        if not head:
          head = ListNode(num)
          temp = head
        else:
          temp.next = ListNode(num)
          temp = temp.next
      
      return head
