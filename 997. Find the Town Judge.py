class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        truster = set()
        trustedBy = defaultdict(list)

        for a, b in trust:
            trustedBy[b].append(a)
            truster.add(a)

        judge = -1

        for person in range(1, n + 1):
            if person not in truster and len(trustedBy[person]) == n - 1:
                judge = person

        return judge
