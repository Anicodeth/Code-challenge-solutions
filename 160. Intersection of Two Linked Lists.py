# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
      visited = set()

      while headA:
        visited.add(id(headA))
        headA = headA.next

      while headB:
        if id(headB) in visited:
          return headB
        headB = headB.next
