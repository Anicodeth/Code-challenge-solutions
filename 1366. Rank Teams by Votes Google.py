class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        
        rank = {letter: [0] * len(votes[0]) for letter in votes[0]}

        for vote in votes:
            for i, letter in enumerate(vote):
                rank[letter][i] += 1

        result = list(rank.items())

        result.sort( key = lambda x: (x[1], -ord(x[0])))
        ans = ""
        for i in range(len(result) - 1, -1, -1):
            ans += result[i][0] 
        
        return ans

