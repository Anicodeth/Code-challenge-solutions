class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        prefix = [0]
        min_ = inf
        
        for block in blocks:
            if block == "B":
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])

        for i in range(len(blocks) - k + 1):
            blacks = prefix[i + k] - prefix[i]
            min_ = min(min_, k - blacks)

        return min_
