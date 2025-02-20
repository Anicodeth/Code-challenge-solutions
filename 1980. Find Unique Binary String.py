class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        hashset = set(nums)
        n = len(nums[0])
        res = ""

        def backtrack(curr):
            nonlocal n, res
            if len(curr) == n:
                possible = "".join(curr)
                if possible not in hashset:
                    res = possible
                
                return

            for c in ["1", "0"]:
                curr.append(c)
                backtrack(curr)
                curr.pop()

        backtrack([])

        return res

