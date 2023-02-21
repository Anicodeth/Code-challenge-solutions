# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if head == None or head.next == None: return None
      temp=head
      start=head
      index=0
      dic={}
      while temp!=None:
        if id(temp) not in dic:
          dic[id(temp)]=index
        elif id(temp) in dic:
          while(id(start)!=id(temp)):
            start=start.next
          return start
        temp=temp.next
        index+=1
      return None
