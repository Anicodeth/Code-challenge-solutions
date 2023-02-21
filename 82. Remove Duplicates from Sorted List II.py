# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def del_first(self,head):
      head=head.next
    def delete_middle(self,node,pre):
      pre.next=node.next


    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if head == None: return head
      elif head.next == None: return head
      dic={}
      temp = head
      while (temp!=None):
        dic[temp.val]= dic.get(temp.val,0)+1
        temp=temp.next

      temp=head
      prev=None

      while temp != None:
        if  dic[temp.val]>1 and prev == None:
          head=head.next
          temp=head
        elif dic[temp.val] > 1:
          node=temp
          temp=temp.next
          self.delete_middle(node,prev)
        else:
          prev=temp
          temp=temp.next

      return head
