# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if not head: return head
      arr = []

      while head:
        arr.append(head.val)
        head = head.next

      odd = even = None

      for i in range(len(arr)-1, -1, -1):
        node = ListNode(arr[i])
        if (i+1) % 2 == 0 :
          print(i)
          node.next = even
          even = node
        else:
          node.next = odd
          odd = node

      temp = odd 

      while temp.next:
        temp = temp.next

      temp.next = even
      return odd


