class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        l = 0

        n = len(s)
        dic = defaultdict(int)
        maxi = -inf
        for r in range(n):
            dic[s[r]] += 1

            while dic[s[r]] > 1:
                dic[s[l]] -= 1
                l += 1

            maxi = max(maxi, (r - l) + 1)

        return maxi

            


        
