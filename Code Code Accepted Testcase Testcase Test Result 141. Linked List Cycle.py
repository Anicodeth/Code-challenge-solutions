# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
      temp = head
      if head == None or head.next == None: return False

      ads = []
      while temp != None:
        
        if id(temp) not in ads:
          ads.append(id(temp))
        else: return True

        temp = temp.next

      return False
