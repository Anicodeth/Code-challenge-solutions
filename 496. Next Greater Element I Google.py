class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        ans = {}
        nums2.reverse()
        for num in nums2:
                while stack and stack[-1] < num:
                    stack.pop()
                if not stack:
                    ans[num] = -1
                else:
                    ans[num] = stack[-1]
                stack.append(num)
                
                

        res = []

        for num in nums1:
            res.append(ans[num])

        return res


        
