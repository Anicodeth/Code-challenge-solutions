# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.n = 0
        self.head = head
        while head:
            self.n += 1
            head = head.next


    def getRandom(self) -> int:
        randomNumber = random.randint(0,self.n - 1)
        temp = self.head
        for _ in range(randomNumber):
            temp = temp.next
        return temp.val

            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
