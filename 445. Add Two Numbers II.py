# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""

        # Helper function to convert a linked list to a string
        def list_to_str(head):
            temp = head
            number = ""
            while temp:
                number += str(temp.val)
                temp = temp.next
            return number

        # Convert the linked lists to strings
        num1 = list_to_str(l1)
        num2 = list_to_str(l2)

        # Calculate the sum as a string
        sum_str = str(int(num1) + int(num2))

        # Initialize the result linked list
        result = ListNode()
        current = result

        # Convert the sum string back to a linked list
        for digit in sum_str:
            current.next = ListNode(int(digit))
            current = current.next

        return result.next 

