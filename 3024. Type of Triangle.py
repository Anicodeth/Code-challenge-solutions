from enum import Enum

class Triangles(Enum):
        EQUILATERAL = "equilateral"
        ISOSCELES = "isosceles"
        SCALENE = "scalene"
        NONE = "none"

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] == nums[1] == nums[2]: 
            return Triangles.EQUILATERAL
        elif nums[2] >= nums[0] + nums[1]:
            return Triangles.NONE
        elif nums[0] == nums[1] or nums[1] == nums[2]:
            return Triangles.ISOSCELES
        else: return Triangles.SCALENE
