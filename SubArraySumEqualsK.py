class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        cursum=0
        pre={0:1}
        for n in nums:
            cursum+=n
            diff= cursum-k

            res+=pre.get(diff,0)
            pre[cursum]=1+pre.get(cursum,0)
        return res
