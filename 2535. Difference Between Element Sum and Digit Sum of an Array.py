class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def addDigits(num):
            dSum = 0
            while num != 0:
                rem = num % 10
                num = num // 10
                dSum += rem

            return dSum
            

        elementSum = sum(nums)
        digitsSum = 0

        for num in nums:
            digitsSum += addDigits(num)

        return abs(digitsSum - elementSum)
