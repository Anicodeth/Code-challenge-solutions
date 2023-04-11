# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      if list2 == None :
        return list1
      
      p1 = list1
      p2 = list2
      temp2 = p2

      while(p1):

        p2 = temp2
        prev = None
        while(p2):
            if p1.val <= p2.val:
              if prev == None:
                n = ListNode(p1.val)
                n.next = p2
                p2 = n
                temp2 = p2
                break

              n = ListNode(p1.val)
              n.next = p2
              prev.next = n
              break

            prev = p2
            p2 = p2.next
            
        if not p2:
          n = ListNode(p1.val)
          prev.next = n

        p1 = p1.next
      return temp2




