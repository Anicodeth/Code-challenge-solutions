# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
      arr = []
      while head:
        arr.append(head.val)
        head = head.next

      arr = arr[:left-1] + arr[left-1:right][::-1] + arr[right:]
      head = None
      for i in range(len(arr) - 1, -1 ,-1):
        node = ListNode(arr[i])
        node.next = head
        head = node

      return head






        

        
        
