class Solution:
    def minOperations(self, k: int) -> int:
        mini  = inf

        for cand in range(1, k + 1):
            positions = ceil(k / cand) - 1
            increase = cand - 1
            mini = min(mini, positions + increase)

        return mini
        
