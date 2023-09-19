class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mini = []
        n = len(nums)
        for num in nums:
            if not mini or mini[-1] > num:
                mini.append(num)
            else:
                mini.append(mini[-1])
        stack = []
        for i in range(n - 1, -1, -1):
            if not stack:
                stack.append(nums[i])
            elif stack[-1] < nums[i]:
                while stack and stack[-1] <= mini[i]:
                    stack.pop()
                if stack and nums[i] > stack[-1]:
                    return True
                else:
                    stack.append(nums[i]) 
            else:
                    stack.append(nums[i]) 

        return False
                
