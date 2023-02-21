# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
      temp=head
      nums=[]
      while temp!=None:
        nums.append(temp.val)
        temp=temp.next
      
      l,r,maxi=0,len(nums)-1,0
      while(l<r):
        if maxi<(nums[r]+nums[l]):
          maxi=nums[r]+nums[l]
        l+=1
        r-=1

      return maxi

      
