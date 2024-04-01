class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        diff = defaultdict(int)
        diff[0] = 1
        curr = 0
        count = 0

        for num in nums:
            curr += num
            
            if curr - k in diff:
                count += diff[curr - k]

            diff[curr] += 1
            
        return count

        
