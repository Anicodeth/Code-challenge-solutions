class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        binary = [ 0 for _ in range(n)]

        for i in range(1, n):
            if nums[i - 1] % 2 == nums[i] % 2:
                binary[i] = 1
        
        prefix = [0]

        for i in range(1, len(binary)):
            prefix.append(prefix[-1] + binary[i])

        ans = []

        for query in queries:
            if prefix[query[1]] - prefix[query[0]] != 0:
                ans.append(False)
            else: ans.append(True)

        return ans
        
