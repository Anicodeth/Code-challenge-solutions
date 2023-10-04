class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0 
        n = len(nums)
        nums.sort()

        def binary_search(start, key):
            l = start
            r = n - 1
            last = inf

            while l <= r:
                m = (l + r) // 2
                

                if nums[m] < key:
                    last = m
                    l = m + 1
                else:
                    r = m - 1

            return 0 if last == inf else (last - start) + 1




        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                count += binary_search(j + 1, nums[i] + nums[j])

        return count
