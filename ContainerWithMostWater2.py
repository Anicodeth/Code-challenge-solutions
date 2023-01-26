class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxi=0

        while (l<r):
            area=(r-l)*min(height[l],height[r])
            if area>maxi:
                maxi=area          
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
                
        return maxi
