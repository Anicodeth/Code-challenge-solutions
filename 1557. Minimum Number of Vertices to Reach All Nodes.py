class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = set(range(n))

        for end in edges:
          if end[1] in incoming:
            incoming.remove(end[1])

        return list(incoming)
