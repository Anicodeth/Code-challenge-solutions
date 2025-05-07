class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dic = defaultdict(int)
        res = 0

        for a, b in dominoes:
            cur = tuple(sorted((a,b)))
            res += dic[cur]
            dic[cur] += 1

        return res
