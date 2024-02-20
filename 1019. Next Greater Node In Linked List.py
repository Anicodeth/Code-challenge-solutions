class Solution:
    def reverse(self,head):
        current=head
        prev=None
        while current != None:
            nex=current.next
            current.next=prev
            prev=current
            current=nex
        head=prev
        return head


    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
      head=self.reverse(head)
      stack=[]
      res=[]
      temp=head
      while temp:
        if len(stack) == 0:
          res.append(0)
        elif stack[-1] > temp.val:
          res.append(stack[-1])
        else:
          while len(stack) > 0 and stack[-1]<=temp.val :
            stack.pop()
          if len(stack)==0:
            res.append(0)
          else:
            res.append(stack[-1])
        stack.append(temp.val)
        temp=temp.next
      return res[::-1]











