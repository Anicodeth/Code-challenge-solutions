class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
      slow=head
      fast=head

      while fast and fast.next:
        fast=fast.next.next if fast.next!=None else None
        slow=slow.next

      return slow
