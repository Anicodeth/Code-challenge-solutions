# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
      lis = []
      for i in range(len(lists)):
        head = lists[i]
        while head:
          lis.append(head.val)
          head = head.next

      heapq.heapify(lis)

      head = ListNode(heapq.heappop(lis)) if lis else None
      temp = head
      while lis:
        node = ListNode(heapq.heappop(lis))
        head.next = node
        head = head.next

      return temp
