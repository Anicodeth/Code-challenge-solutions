class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        l, r = 0, len(arr) - 1
        n = len(arr) - 1

        while l <= r:

            m = (l + r) // 2

            if ((m - 1 < l) or (arr[m-1] <= arr[m])) and ((m + 1 > r) or (arr[m + 1] <= arr[m])):
                return m
            
            elif m - 1 >= l and arr[m - 1] > arr[m]:
                r = m - 1
            
            elif m + 1 <= r and arr[m + 1] > arr[m]:
                l = m + 1

        
