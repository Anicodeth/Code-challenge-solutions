class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False

        peak=max(arr)
        peak_index=arr.index(peak)

        if(peak_index==len(arr)-1 or peak_index==0):
            return False

        for i in range(peak_index-1):
            if(arr[i+1]<=arr[i]):
                return False

        for j in range(peak_index,len(arr)-1):
            if(arr[j+1]>=arr[j]):
                return False

        return True
