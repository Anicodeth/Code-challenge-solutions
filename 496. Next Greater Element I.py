class Solution:
    def nextGreaterElement(self,nums1, nums2):
        stack = []
        nextGreater = {}

        for num in nums2[::-1]:
            while stack and num > stack[-1]:
                stack.pop()
            if stack:
                nextGreater[num] = stack[-1]
            else:
                nextGreater[num] = -1
            stack.append(num)

        ans = []
        for num in nums1:
            ans.append(nextGreater[num])

        return ans
