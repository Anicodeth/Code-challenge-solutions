class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        maxi = -1

        for key in count:
            if count[key] == key: maxi = max(maxi, key)

        return maxi     
