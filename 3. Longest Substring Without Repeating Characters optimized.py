class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        start = 0
        end = 0
        maxi = -inf


        for i,c in enumerate(s):
            if c in last:
                start = max(start, last[c] + 1)

            last[c] = i
            end = i
            maxi = max(end - start + 1, maxi)

        return maxi if maxi != -inf else 0
