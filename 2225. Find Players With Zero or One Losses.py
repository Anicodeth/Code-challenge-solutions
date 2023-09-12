class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        results = {}

        for winner, loser in matches:
            results[loser] = results.get(loser, 0) + 1
            results[winner] = results.get(winner, 0)
        zero_loss = []
        one_loss = []
        for player in results:
            if results[player] == 0:
                zero_loss.append(player)
            elif results[player] == 1:
                one_loss.append(player)
        zero_loss.sort()
        one_loss.sort()
        return [zero_loss, one_loss]
