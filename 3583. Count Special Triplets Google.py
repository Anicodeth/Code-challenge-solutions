class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        forwardDict = defaultdict(int)
        backwardDict = Counter(nums)
        count = 0 

        for num in nums:
            backwardDict[num] -= 1

            value = num * 2
            left = forwardDict[value]
            right = backwardDict[value]
            count += left * right

            forwardDict[num] += 1

        return count % (10**9 + 7)
