class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        res = []
        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(even.pop())
            else:
                res.append(odd.pop())

        return res


        
