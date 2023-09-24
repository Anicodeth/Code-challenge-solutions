class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dic = {}

        for num in nums:
            if num % 2 == 0:
                dic[num] = dic.get(num, 0) + 1

        if not dic:
            return -1

        values = list(dic.items())
        values.sort(key = lambda x: (-x[1], x[0]))
        return values[0][0]     
