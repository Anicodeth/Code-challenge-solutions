class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

      res = []
      def dfs(start, sumi, arr):
        nonlocal res
        if target == sumi:
          res.append(arr)
        if target < sumi:
          return

        for i in range(start, len(candidates)):
          dfs(i, sumi + candidates[i], arr + [candidates[i]])
      dfs(0,0,[])

      return res
