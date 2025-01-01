class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack = []
        ans = []

        for i in range(n - 1, -1, -1):

            while stack and stack[-1] > prices[i]:
                stack.pop()

            if stack: ans.append(prices[i] - stack[-1])
            else: ans.append(prices[i])

            stack.append(prices[i])

        return ans[::-1]
