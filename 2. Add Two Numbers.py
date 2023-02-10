
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def addTwoNumbers(self, l1, l2):
        self.head=ListNode(10)
        remain=0
        while(l1!=None or l2!=None):
            if(l1==None):
                self.addtail(ListNode((l2.val+remain)%10))
                remain=(l2.val+remain)//10
                l2=l2.next
            elif(l2==None):
                self.addtail(ListNode((l1.val+remain)%10))
                remain=(l1.val+remain)//10
                l1=l1.next
            else:
                self.addtail(ListNode((l1.val+l2.val+remain)%10))
                remain=(l1.val+l2.val+remain)//10
                l1=l1.next
                l2=l2.next
            print(remain)
        if(remain!=0):
            self.addtail(ListNode(remain))
        return self.head


    def addtail(self,node):
        if(self.head.val==10):
            self.head=node
        else:
            last=self.head
            while(last.next!=None):
                last=last.next
            last.next=node
