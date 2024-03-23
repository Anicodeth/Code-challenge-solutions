class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        n = len(candidates)

        def backtrack(index, curr, sumi):
            nonlocal n
            if sumi == target:
                res.append(curr[:])
                return

            if sumi > target:
                return

            for i in range(index, n):
                curr.append(candidates[i])
                backtrack(i, curr, sumi + candidates[i])
                curr.pop()

            
        backtrack(0, [], 0)

        return res 
