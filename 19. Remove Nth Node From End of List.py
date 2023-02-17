# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        count=0
        while temp!=None:
            count+=1
            temp=temp.next

        if count==1 and n==1: return None
        elif count-n==0: 
            head=head.next 
            return head


        prev=head
        current=head.next
        for _ in range(count-n-1):
            prev=prev.next
        current=prev.next
        temp=current.next if current!=None else None
        prev.next=temp

        return head



