class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        items = list(count.items())
        items.sort(key = lambda x: (x[1], -x[0]))
        res = []

        for item in items:
            res.extend([item[0]] * item[1])

        return res

        
