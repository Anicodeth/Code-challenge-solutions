class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        res = []

        for child in candies:
            if child + extraCandies >= maxi:
                res.append(True)
            else: res.append(False)

        return res
        
