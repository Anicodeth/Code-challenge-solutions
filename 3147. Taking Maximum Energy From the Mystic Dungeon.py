class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)

        for i in range(n - 1, -1, -1):
            if i + k >= n: 
                continue

            energy[i] += energy[i + k]

        return max(energy)
        
