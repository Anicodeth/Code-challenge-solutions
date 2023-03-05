class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
      
        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target and target < nums[mid+1]:
                return mid+1
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid
        return low+1
