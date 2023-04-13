# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      res = None

      while head:
        inserted = False
        node = ListNode(head.val)
        if not res:
          node.next = res
          res = node
          inserted = True
        else:
          temp = res
          prev = None 
          while temp:
            if temp.val >= node.val:
              if prev == None:
                node.next = res
                res = node
                inserted = True
                break
              else:
                node.next = temp
                prev.next = node
                inserted = True
                break

            prev = temp
            temp = temp.next
        if not inserted:
          node.next = temp
          prev.next = node


        head = head.next

      return res
