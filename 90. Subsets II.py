class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        counter = []
        res = []
        def backtrack(curr, index):
            nonlocal counter, res
            if index == n + 1:
                return
            table = Counter(curr)
            if  table not in counter:
                 counter.append(table)
                 res.append(curr[:])

            for i in range(index, n):
                curr.append(nums[i])
                backtrack(curr, i + 1)
                curr.pop()

        backtrack([],0)

        return res

        
        
