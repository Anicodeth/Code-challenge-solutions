class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        n = len(nums)

        def backtrack(curr, i):
            if i == n:
                return 

            for j in range(i + 1, n):
                curr.append(nums[j])
                res.append(curr[:])
                backtrack(curr, j)
                curr.pop()

        
        for i in range(n):
            res.append([nums[i]])
            backtrack([nums[i]], i)

        return res

