class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        nums = [-a, -b, -c]
        heapq.heapify(nums)

        score = 0

        while True:
            one = heapq.heappop(nums)
            two = heapq.heappop(nums)

            if one == 0 or two == 0:
                break

            score += 1
            heapq.heappush(nums, one + 1)
            heapq.heappush(nums, two + 1)

        return score

        

        
