class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0]*(n+1)
        for i, j in requests:
            freq[i] += 1
            freq[j + 1] -= 1
        for i in range(1, n + 1):
            freq[i] += freq[i - 1]
        freq.sort(reverse=True)
        nums.sort(reverse=True)
        
        total = 0
        for i in range(n):
            if freq[i]:
                total +=  (nums[i] * freq[i]) % 1000000007
            else:
                break
        return total%1000000007
