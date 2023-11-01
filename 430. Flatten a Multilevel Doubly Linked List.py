"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        order = []

        visited = set()
        stack = [ head ]

        while stack:
            parent = stack.pop()
            while parent:
                if parent.child and id(parent) not in visited:
                    order.append(parent.val)
                    stack.append(parent)
                    visited.add(id(parent))
                    stack.append(parent.child)
                    break
                if id(parent) not in visited:
                    order.append(parent.val)
                parent = parent.next

        head = temp = prev = None
        for num in order:
            if not head:
                head = Node(num, None, None, None)
                temp = head
                prev = head
            else:
                temp.next = Node(num, None, None, None)
                temp = temp.next
                temp.prev = prev
                prev = temp
                

        return head
