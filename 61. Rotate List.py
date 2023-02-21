# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def delete_last(self,head):
    prev=head
    current=head.next 
    while current.next != None:

      prev=prev.next
      current=current.next 

    prev.next=None
    return current

  def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    count=0
    p=head
    while p != None:
      count+=1
      p=p.next
    if head == None or head.next == None: return head
    for _ in range(k%count):    
      cur= self.delete_last(head)
      cur.next=head
      head=cur
    return head

