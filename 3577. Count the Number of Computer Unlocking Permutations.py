class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        start = complexity[0]
        n = len(complexity)

        for i in range(1, n):
            if complexity[i] <= start:
                return 0

        def factorial(n):
            if n == 0: return 1
            return n * factorial(n - 1)

        return factorial(n - 1) % (10**9 + 7)  
