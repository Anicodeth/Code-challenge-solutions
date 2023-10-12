class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        peak_index = self.findPeak(mountain_arr, length)
        result = self.searchIncreasing(mountain_arr, target, peak_index)
        if result != -1:
            return result
        result = self.searchDecreasing(mountain_arr, target, peak_index, length)
        return result

    def findPeak(self, mountain_arr, length):
        low = 1
        high = length - 2
        while low != high:
            test_index = (low + high) // 2
            if mountain_arr.get(test_index) < mountain_arr.get(test_index + 1):
                low = test_index + 1
            else:
                high = test_index
        return low

    def searchIncreasing(self, mountain_arr, target, peak_index):
        low = 0
        high = peak_index
        while low != high:
            test_index = (low + high) // 2
            if mountain_arr.get(test_index) < target:
                low = test_index + 1
            else:
                high = test_index
        if mountain_arr.get(low) == target:
            return low
        return -1

    def searchDecreasing(self, mountain_arr, target, peak_index, length):
        low = peak_index + 1
        high = length - 1
        while low != high:
            test_index = (low + high) // 2
            if mountain_arr.get(test_index) > target:
                low = test_index + 1
            else:
                high = test_index
        if mountain_arr.get(low) == target:
            return low
        return -1
