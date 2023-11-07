class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner = arr[0]
        wins = 0

        for i in range(1, len(arr)):
            if winner < arr[i]:
                wins = 1
                winner = arr[i]
            else:
                wins += 1

            if wins == k:
                return winner

        return winner
