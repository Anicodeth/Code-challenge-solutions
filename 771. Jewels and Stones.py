class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = Counter(stones)

        ans = 0

        for jewel in jewels:
            if jewel in counter:
                ans += counter[jewel]

        return ans
