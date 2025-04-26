class Solution:
    def countLargestGroup(self, n: int) -> int:

        dic = {}

        def addDigits(num):
            sumi = 0

            while num:
                rem = num % 10
                num //= 10
                sumi += rem
            
            return sumi

        for num in range(1, n + 1):
            sumi = addDigits(num)
            dic[sumi] = dic.get(sumi, 0) + 1

        pairs = list(dic.items())
        pairs.sort(key = lambda x : -x[1])

        largest = pairs[0][1]
        count = 0
        for pair in pairs:
            if pair[1] == largest:
                count += 1

        return count
