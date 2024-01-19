class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        UNMs  = defaultdict(set)
        for ID, time in logs:
            UNMs[ID].add(time)

        ans = [0] * k

        for checkin in UNMs.values():
            ans[len(checkin) - 1] += 1

        return ans

